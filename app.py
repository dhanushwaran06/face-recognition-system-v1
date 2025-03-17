from flask import Flask, render_template
from routes.student_routes import student_routes

app = Flask(__name__, template_folder="templates", static_folder="static")

# ✅ Register the student_routes Blueprint
app.register_blueprint(student_routes)  

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
