class Book:
    def __init__(self, resource_id, title, subject, available=True):
        self.resource_id = resource_id
        self.title = title
        self.subject = subject
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Unavailable"
        return f"Book, {self.title}, ({self.subject}) - {status}"

books_list = [
    Book("B001", "Introduction to Python", "Programming"),
    Book("B002", "Basics of SQL", "Database"),
    Book("B003", "Artificial Intelligence Basics", "AI"),
    Book("B004", "Introduction to Java", "Programming"),
    Book("B005", "Basic Maths", "Mathematics"),
    Book("B006", "Discrete Maths", "Mathematics"),
    Book("B007", "Advance database", "Database"),
    Book("B008", "Data Science Handbook", "Data Science"),
    Book("B009", "Introduction to Law", "Law")
] 