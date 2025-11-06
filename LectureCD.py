class LectureCD:
    def __init__(self, resource_id, title, subject, available=True):
        self.resource_id = resource_id
        self.title = title
        self.subject = subject
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Unavailable"
        return f"Lecture CD, {self.title}, ({self.subject}) - {status}"

cd_list = [
    LectureCD("C001", "Database Design Lecture", "Database"),
    LectureCD("C002", "Software Engineering Concepts", "Software Engineering"),
    LectureCD("C003", "Database Coding Lecture", "Database"),
    LectureCD("C004", "Flowchart explanations", "Software Engineering"),
    LectureCD("C005", "Explanation of MySql", "Databases")
]