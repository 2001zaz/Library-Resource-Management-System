from book import Book, books_list
from magazine import Magazine, magazines_list
from dvd import DVD, dvds_list
from LectureCD import LectureCD, cd_list

class Library:
    def __init__(self):
        self.resources = books_list + magazines_list + dvds_list + cd_list

    def add_resource(self, resource):
        self.resources.append(resource)
        print(f"\n Resource '{resource.title}' added successfully!")

    def view_resources(self, resource_type=None, subject=None, only_available=None):
        print("\nLibrary Resources")
        print("\n(ResourceType, Title, Available or Not)")
        for res in self.resources:
            if resource_type and res.__class__.__name__.lower() != resource_type.lower():
                continue
            if subject and res.subject.lower() != subject.lower():
                continue
            if only_available is not None and res.available != only_available:
                continue
            print(res)
        print()

    def update_availability(self, resource_id, status):
        for res in self.resources:
            if res.resource_id == resource_id:
                res.available = status
                print(f"\n Updated '{res.title}' to {'Available' if status else 'Unavailable'}")
                return
        print("\n Resource not found!")

    def delete_resource(self, resource_id):
        for res in self.resources:
            if res.resource_id == resource_id:
                self.resources.remove(res)
                print(f"\n Resource '{res.title}' deleted successfully.")
                return
        print("\n Resource not found!")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Resource")
        print("2. View All Resources")
        print("3. View Available Resources by Type or Subject")
        print("4. Update Resource Availability")
        print("5. Delete Resource")
        print("6. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            rid = input("Enter Resource ID: ")
            title = input("Enter Title: ")
            subject = input("Enter Subject: ")
            print("Select Resource Type:")
            print("1. Book\n2. Magazine\n3. Educational DVD\n4. Lecture CD")
            type_choice = input("Enter choice: ")

            if type_choice == '1':
                resource = Book(rid, title, subject)
            elif type_choice == '2':
                resource = Magazine(rid, title, subject)
            elif type_choice == '3':
                resource = DVD(rid, title, subject)
            elif type_choice == '4':
                resource = LectureCD(rid, title, subject)
            else:
                print("\n Invalid resource type!")
                continue

            library.add_resource(resource)

        elif choice == '2':
            library.view_resources()

        elif choice == '3':
            rtype = input("Enter Type (Book/Magazine/DVD/LectureCD) or leave blank: ").strip() or None
            subject = input("Enter Subject or leave blank: ").strip() or None
            library.view_resources(resource_type=rtype, subject=subject, only_available=True)

        elif choice == '4':
            rid = input("Enter Resource ID to update: ")
            status = input("Enter new status (available/unavailable): ").lower() == "available"
            library.update_availability(rid, status)

        elif choice == '5':
            rid = input("Enter Resource ID to delete: ")
            library.delete_resource(rid)

        elif choice == '6':
            print("\n Exiting Library Management System. Goodbye! Have a nice Day")
            break

        else:
            print("\n Invalid choice! Try again.")


if __name__ == "__main__":
    main()
