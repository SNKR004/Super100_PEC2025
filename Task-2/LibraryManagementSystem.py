class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.books = []

    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Books: {[book.title for book in self.books]}")


class Book:
    def __init__(self, id, title, avail):
        self.id = id
        self.title = title
        self.avail = avail

    def display(self):
        print(f"ID: {self.id}")
        print(f"Title: {self.title}")
        print(f"Available: {self.avail}")


class Library:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.books = []

    def add_member(self, member):
        self.members.append(member)
        print(f"Member {member.name} added to {self.name} library!")

    def remove_member(self, member):
        self.members.remove(member)
        print(f"Member {member.name} removed from {self.name} library!")

    def display_members(self):
        print(f"Members in {self.name}:")
        for member in self.members:
            member.display()
            print()

    def add_book(self, book):
        self.books.append(book)
        print(f"Book {book.title} added to {self.name} library!")

    def remove_book(self, book):
        self.books.remove(book)
        print(f"Book {book.title} removed from {self.name} library!")

    def display_books(self):
        print(f"Books in {self.name}:")
        for book in self.books:
            book.display()
            print()

    def search_member_by_id(self, id):
        for member in self.members:
            if member.id == id:
                return member
            return None
        
    def search_book_by_id(self, id):
        for book in self.books:
            if book.id == id:
                return book
            return None
        
    def borrow_book(self, book, member):
        if book.avail:
            book.avail = False
            member.books.append(book)
            print(f"Book {book.title} borrowed by {member.name}!")
        else:
            print(f"Book {book.title} is not available!")

    def return_book(self, book, member):
        if book in member.books:
            book.avail = True
            member.books.remove(book)
            print(f"Book {book.title} returned by {member.name}!")
        else:
            print(f"Book {book.title} is not borrowed by {member.name}")

def main():
    book1 = Book("B01", "Data Structures and Algorithms", True)
    book2 = Book("B02","Machine Learning", True)
    book3 = Book("B03", "Database Management Systems", True)
    book4 = Book("B04", "Computer Organization", True)
    book5 = Book("B05", "Operating Systems", True)

    library = Library("PEC")

    member1 = Member("21314254", "Sankar Addala")
    member2 = Member("21314200", "Builer Bob")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)

    library.add_member(member1)
    library.add_member(member2)

    library.display_books()
    library.display_members()

    library.borrow_book(book1, member1)
    library.borrow_book(book3, member1)
    library.borrow_book(book4, member2)
    library.borrow_book(book2, member2)

    library.return_book(book4, member2)

    library.display_books()
    library.display_members()

if __name__ == "__main__":
    main()
