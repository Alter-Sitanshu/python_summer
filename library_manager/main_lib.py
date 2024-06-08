import librarydoc


print(librarydoc.logo)
enter = input("Login to the library ?(yes/no) : ").lower()
if enter == "yes":
    enter = True
else:
    enter = False
action_func = {"add": librarydoc.add_book,
               "delete": librarydoc.delete_book,
               "view": librarydoc.view_books,
               }
while enter:
    user = input("Enter your username : ").lower()
    pasw = input("Enter your password : ")
    login = librarydoc.Library(user=user,password=pasw)
    check = login.login()
    if check == 0:
        print("Logging out from Library ...")
        break
    specific_functions = {"issue": login.issue_book, "return" : login.return_book}
    print("General actions avaialable are : add book, delete book, view book\n")
    action = input("What do you want to do ? : ")
    if action == "add":
        book_name = input("Enter book name : ").lower()
        author = input("Enter book author : ").lower()
        action_func[action](book_name=book_name,author=author)
    elif action == "delete":
        book_name = input("Enter book name : ").lower()
        action_func[action](book_name=book_name)
    elif action == "view":
        action_func[action]()
    else:
        print("User specific actions are : issue book, return book")
        specific_func = input("What do you want to do ? : ")
        if specific_func == "issue":
            book_name = input("Enter book name : ").lower()
            specific_functions[specific_func](book_name=book_name)
        elif specific_func == "return":
            book_name = input("Enter book name : ").lower()
            specific_functions[specific_func](book_name=book_name)
        else:
            print("Desired action is not avaialable currently ! Sorry")
            enter = False
            break
    enter = input("Do you want to login again ?(yes/no) : ").lower()
    if enter == "yes":
        enter = True
    else:
        break