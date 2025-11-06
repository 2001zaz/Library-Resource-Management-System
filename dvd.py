class DVD:
    def __init__(self, resource_id, title, subject, available=True):
        self.resource_id = resource_id
        self.title = title
        self.subject = subject
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Unavailable"
        return f"Educational DVD, {self.title}, ({self.subject}) - {status}"

dvds_list = [
    DVD("D001", "Machine Learning Crash Course", "AI"),
    DVD("D002", "Python for Beginners", "Programming"),
    DVD("D003", "ER diagram explanation", "Database"),
    DVD("D004", "Introduction to Java", "Programming"),
    DVD("D005", "Basics of SQL", "Database")
]
