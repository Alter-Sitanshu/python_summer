lib_books = {"roman invasion":{"name":"roman invasion", "author": "paul strauss"}}
lib_users = {"sitanshu":"1234", "muskan":"hello", "steel":"iron"}

class Library:
    def __init__(self, user, password) :
        self.user = user
        self.password = password
        self.books = {}
    def login(self):
        if self.user in lib_users:
            if lib_users[self.user] == self.password:
                print(f"Welcome to the library !")
            else:
                print(f"Wrong password for {self.user}")
                return 0
        else:
            register = input("You are not a member, want to Register ?(yes/no) : ").lower()
            if register == "yes":
                lib_users[self.user] = self.password
                print("New memeber added successfully !")
            else:
                return 0
    
    def issue_book(self, book_name):
        self.books[book_name] = lib_books[book_name]
        delete_book(book_name)
    
    def return_book(self, book_name):
        book = self.books[book_name]
        del self.books[book_name]
        add_book(book["name"], book["author"])

def add_book(book_name, author):
        if book_name not in lib_books:
            lib_books[book_name] = {"name":book_name, "author":author}
            print(f"Thank you for submission, the book '{book_name}' has been added !")
        else:
            print("The book already exists, Thank you !")
    
def delete_book(book_name):
    if book_name in lib_books:
        del lib_books[book_name]
    else:
        print(f"The book '{book_name}' is not available in the library !")
def view_books():
    print("We have the following books :")
    for books in lib_books:
        print(books)

logo = """
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |   _____      | || |     _____    | || |   ______     | || |  _______     | || |      __      | || |  _______     | || |  ____  ____  | |
| |  |_   _|     | || |    |_   _|   | || |  |_   _ \    | || | |_   __ \    | || |     /  \     | || | |_   __ \    | || | |_  _||_  _| | |
| |    | |       | || |      | |     | || |    | |_) |   | || |   | |__) |   | || |    / /\ \    | || |   | |__) |   | || |   \ \  / /   | |
| |    | |   _   | || |      | |     | || |    |  __'.   | || |   |  __ /    | || |   / ____ \   | || |   |  __ /    | || |    \ \/ /    | |
| |   _| |__/ |  | || |     _| |_    | || |   _| |__) |  | || |  _| |  \ \_  | || | _/ /    \ \_ | || |  _| |  \ \_  | || |    _|  |_    | |
| |  |________|  | || |    |_____|   | || |  |_______/   | || | |____| |___| | || ||____|  |____|| || | |____| |___| | || |   |______|   | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
"""