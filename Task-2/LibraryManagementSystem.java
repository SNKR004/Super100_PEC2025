import java.util.*;


class Member {
    private String id;
    private String name;
    private ArrayList<Book> books;

    public Member(String id, String name) {
        this.id = id;
        this.name = name;
        this.books = new ArrayList<Book>();
    }

    public void display() {
        System.out.println("ID: " + this.id);
        System.out.println("Name: " + this.name);
        System.out.println("Books: " + this.getBookTitles());
    }

    private String getBookTitles() {
        String titles = "[";
        for (int i = 0; i < this.books.size(); i++) {
            titles += this.books.get(i).getTitle();
            if (i < this.books.size() - 1) {
                titles += ", ";
            }
        }
        titles += "]";
        return titles;
    }

    public String getId() {
        return this.id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ArrayList<Book> getBooks() {
        return this.books;
    }

    public void setBooks(ArrayList<Book> books) {
        this.books = books;
    }
}


class Book {
    private String id;
    private String title;
    private boolean avail;

    public Book(String id, String title, boolean avail) {
        this.id = id;
        this.title = title;
        this.avail = avail;
    }

    public void display() {
        System.out.println("ID: " + this.id);
        System.out.println("Title: " + this.title);
        System.out.println("Available: " + this.avail);
    }

    public String getId() {
        return this.id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getTitle() {
        return this.title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public boolean isAvail() {
        return this.avail;
    }

    public void setAvail(boolean avail) {
        this.avail = avail;
    }
}


class Library {
    private String name;
    private ArrayList<Member> members;
    private ArrayList<Book> books;

    public Library(String name) {
        this.name = name;
        this.members = new ArrayList<Member>();
        this.books = new ArrayList<Book>();
    }

    public void addMember(Member member) {
        this.members.add(member);
        System.out.println("Member " + member.getName() + " added to " + this.name + " library!");
    }

    public void removeMember(Member member) {
        this.members.remove(member);
        System.out.println("Member " + member.getName() + " removed from " + this.name + " library!");
    }

    public void displayMembers() {
        System.out.println("Members in " + this.name + ":");
        for (Member member : this.members) {
            member.display();
            System.out.println();
        }
    }

    public void addBook(Book book) {
        this.books.add(book);
        System.out.println("Book " + book.getTitle() + " added to " + this.name + " library!");
    }

    public void removeBook(Book book) {
        this.books.remove(book);
        System.out.println("Book " + book.getTitle() + " removed from " + this.name + " library!");
    }

    public void displayBooks() {
        System.out.println("Books in " + this.name + ":");
        for (Book book : this.books) {
            book.display();
            System.out.println();
        }
    }

    public Member searchMemberById(String id) {
        for (Member member : this.members) {
            if (member.getId().equals(id)) {
                return member;
            }
        }
        return null;
    }

    public Book searchBookById(String id) {
        for (Book book : this.books) {
            if (book.getId().equals(id)) {
                return book;
            }
        }
        return null;
    }

    public void borrowBook(Book book, Member member) {
        if (book.isAvail()) {
            book.setAvail(false);
            member.getBooks().add(book);
            System.out.println("Book " + book.getTitle() + " borrowed by " + member.getName() + "!");
        } else {
            System.out.println("Book " + book.getTitle() + " is not available!");
        }
    }

    public void returnBook(Book book, Member member) {
        if (member.getBooks().contains(book)) {
            book.setAvail(true);
            member.getBooks().remove(book);
            System.out.println("Book " + book.getTitle() + " returned by " + member.getName() + "!");
        } else {
            System.out.println("Book " + book.getTitle() + " is not borrowed by " + member.getName());
        }
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ArrayList<Member> getMembers() {
        return this.members;
    }

    public void setMembers(ArrayList<Member> members) {
        this.members = members;
    }

    public ArrayList<Book> getBooks() {
        return this.books;
    }

    public void setBooks(ArrayList<Book> books) {
        this.books = books;
    }
}


class Main {
    public static void main(String[] args) {
        Book book1 = new Book("B01", "Data Structures and Algorithms", true);
        Book book2 = new Book("B02","Machine Learning", true);
        Book book3 = new Book("B03", "Database Management Systems", true);
        Book book4 = new Book("B04", "Computer Organization", true);
        Book book5 = new Book("B05", "Operating Systems", true);

        Library library = new Library("PEC");

        Member member1 = new Member("21314254", "Sankar Addala");
        Member member2 = new Member("21314200", "Builer Bob");

        library.addBook(book1);
        library.addBook(book2);
        library.addBook(book3);
        library.addBook(book4);
        library.addBook(book5);

        library.addMember(member1);
        library.addMember(member2);

        library.displayBooks();
        library.displayMembers();

        library.borrowBook(book1, member1);
        library.borrowBook(book3, member1);
        library.borrowBook(book4, member2);
        library.borrowBook(book2, member2);

        library.returnBook(book4, member2);

        library.displayBooks();
        library.displayMembers();
    }
}

/*
Output:

Book Data Structures and Algorithms added to PEC library!
Book Machine Learning added to PEC library!
Book Database Management Systems added to PEC library!
Book Computer Organization added to PEC library!
Book Operating Systems added to PEC library!
Member Sankar Addala added to PEC library!
Member Builer Bob added to PEC library!
Books in PEC:
ID: B01
Title: Data Structures and Algorithms
Available: true

ID: B02
Title: Machine Learning
Available: true

ID: B03
Title: Database Management Systems
Available: true

ID: B04
Title: Computer Organization
Available: true

ID: B05
Title: Operating Systems
Available: true

Members in PEC:
ID: 21314254
Name: Sankar Addala
Books: []

ID: 21314200
Name: Builer Bob
Books: []

Book Data Structures and Algorithms borrowed by Sankar Addala!
Book Database Management Systems borrowed by Sankar Addala!
Book Computer Organization borrowed by Builer Bob!
Book Machine Learning borrowed by Builer Bob!
Book Computer Organization returned by Builer Bob!
Books in PEC:
ID: B01
Title: Data Structures and Algorithms
Available: false

ID: B02
Title: Machine Learning
Available: false

ID: B03
Title: Database Management Systems
Available: false

ID: B04
Title: Computer Organization
Available: true

ID: B05
Title: Operating Systems
Available: true

Members in PEC:
ID: 21314254
Name: Sankar Addala
Books: [Data Structures and Algorithms, Database Management Systems]

ID: 21314200
Name: Builer Bob
Books: [Machine Learning]

*/
