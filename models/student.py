class Student:
    def __init__(self, name, student_id, student_class, face_encoding):
        self.name = name
        self.id = student_id
        self.class_name = student_class
        self.face_encoding = face_encoding

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "class": self.class_name,
            "face_encoding": self.face_encoding
        }
