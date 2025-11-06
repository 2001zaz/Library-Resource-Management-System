class Magazine:
    def __init__(self, resource_id, title, subject, available=True):
        self.resource_id = resource_id
        self.title = title
        self.subject = subject
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Unavailable"
        return f"Magazine, {self.title}, ({self.subject}) - {status}"

magazines_list = [
    Magazine("M001", "Tech Monthly", "Technology"),
    Magazine("M002", "Science Weekly", "Research"),
    Magazine("M003", "TechMag", "Technology"),
    Magazine("M004", "Research on employees", "Research")
]