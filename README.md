# Student Face Recognition System 🚀  

A Flask-based student identification system using **face recognition** and **MongoDB**.  

## Features  
✅ Add students with their images & face encodings  
✅ Search for students using an image  
✅ Securely stores face encodings in MongoDB  
✅ Flask REST API for easy integration  

## Installation  

1. **Clone the Repository**  
   ```sh
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

2. **Set Up Virtual Environment & Install Dependencies**  
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Flask App**  
   ```sh
   python app.py
   ```

## API Endpoints  

| Method | Endpoint        | Description |
|--------|---------------|-------------|
| POST   | `/add_student` | Add a student with an image |
| POST   | `/search`      | Search for a student by image |

## Tech Stack  
- **Python** (Flask)  
- **MongoDB** (Database)  
- **face_recognition** (Face detection & encoding)  


