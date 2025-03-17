from flask import Blueprint, request, jsonify
from database.connection import db
from models.student import Student
import face_recognition
import os
import numpy as np

student_routes = Blueprint("student_routes", __name__)

UPLOAD_FOLDER = "uploads/"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

# Ensure the uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@student_routes.route("/add_student", methods=["POST"])
def add_student():
    print("Received request to add student")

    if "image" not in request.files or "name" not in request.form or "id" not in request.form or "class" not in request.form:
        print("Missing data:", request.form, request.files)  # Debugging
        return jsonify({"error": "Missing data"}), 400

    file = request.files["image"]
    name = request.form["name"]
    student_id = request.form["id"]
    student_class = request.form["class"]

    print(f"Received: name={name}, id={student_id}, class={student_class}, file={file.filename}")

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    image = face_recognition.load_image_file(filepath)
    encodings = face_recognition.face_encodings(image)

    if len(encodings) == 0:
        print("No face detected")
        return jsonify({"error": "No face detected"}), 400

    encoding = encodings[0].tolist()  # Convert to list for MongoDB

    student = {
        "name": name,
        "id": student_id,
        "class": student_class,
        "encoding": encoding
    }

    db["students"].insert_one(student)
    
    print("✅ Student added successfully with encoding")
    return jsonify({"message": "Student added successfully"})

@student_routes.route("/search", methods=["POST"])
def search_student():
    print("Received search request")

    if "image" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["image"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    image = face_recognition.load_image_file(filepath)
    encodings = face_recognition.face_encodings(image)

    if len(encodings) == 0:
        return jsonify({"error": "No face detected"}), 400

    encoding = encodings[0]
    print("Input Encoding (first 5 values):", encoding[:5])  # Debug

    students = list(db["students"].find({}))
    print(f"Total students in DB: {len(students)}")

    best_match = None
    best_distance = float("inf")

    for student in students:
        if "encoding" not in student:
            print(f"Skipping {student.get('name', 'Unknown')} - No encoding found.")
            continue

        known_encoding = np.array(student["encoding"])
        print(f"Checking against {student['name']}, Encoding (first 5 values):", known_encoding[:5])

        matches = face_recognition.compare_faces([known_encoding], encoding, tolerance=0.6)
        distance = face_recognition.face_distance([known_encoding], encoding)[0]
        print(f"Face Distance for {student['name']}: {distance}")

        if matches[0] and distance < best_distance:
            best_match = student
            best_distance = distance

    if best_match:
        return jsonify({
            "name": best_match["name"],
            "id": best_match["id"],
            "class": best_match["class"]
        })

    return jsonify({"error": "No matching student found"}), 404
