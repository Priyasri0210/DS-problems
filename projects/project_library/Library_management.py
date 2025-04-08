import json
#from collections import defaultdict
def load_data():
    with open('C:/Users/DELL/OneDrive/Desktop/demo-repo/DS-problems/projects/project_library/Library.json','r') as f:
        book_db = json.load(f)
        return book_db
        
def save_data(data):
    with open('C:/Users/DELL/OneDrive/Desktop/demo-repo/DS-problems/projects/project_library/Library.json','w') as f:
        json.dump(data,f)

def add_book(book_db,Borrowed=0):
    try:
        ISBN_no = (input("Enter ISBN_no: "))
        
        if ISBN_no in book_db:
            print('ISBN_no is already registered')
            return None
        
        Title = input("Enter Book title : ")
        Author= input('Enter Author name : ')
        Genre = input("Enter Book Genre : ")
        Copies = int(input('Enter no.of copies : '))
        
        book_db[ISBN_no] = {"Title":Title,"Author":Author,"Genre":Genre,"Copies":Copies,"Borrowed":Borrowed}
        save_data(book_db)
        print('Book registered successfully')
    except Exception as e:
        print('error in adding book')
        print(e)

def search_book(book_db):
    ISBN_no = input("Enter the ISBN_no to be searched : ")
    if ISBN_no in book_db:
        print("Details : ")
        print(book_db[ISBN_no])
    else:
        print('Book is not available')

def update_book(book_db):
    ISBN_no = input("Enter the ISBN_no to be updated : ")
    if ISBN_no not in book_db:
        print("Book is not available")
    else:
        Title = input("Enter Book title : ")
        Author= input('Enter Author name : ')
        Genre = input("Enter Book Genre : ")
        Copies = int(input('Enter no.of copies : '))
        Borrowed = int(input("No. of copies borrowed: "))
        book_db[ISBN_no] = {"Title":Title,"Author":Author,"Genre":Genre,"Copies":Copies,"Borrowed":Borrowed}
        save_data(book_db)
        print('Book details updated successfully')

def delete_book(book_db):
    ISBN_no = input("Enter the ISBN_no to be deleted : ")
    if ISBN_no not in book_db:
        print("Book is not available")
    else:
        del book_db[ISBN_no]
        save_data(book_db)
        print('Book deleted successfully')

def view_books(book_db):
    if book_db:
        for ISBN, details in book_db.items():
            print("ISBN_no : {}, Title : {}, Author : {}, Genre : {}, Copies : {}, Borrowed : {}".format(ISBN,details['Title'],details['Author'],details['Genre'],details['Copies'],details['Borrowed']))
    else:
        print('No books in database')

def check_out_book(book_db):
    ISBN_no = input("Enter the ISBN_no of book to be borrow : ")
    if ISBN_no not in book_db:
        print("Book is not available")
        return
    elif book_db[ISBN_no]["Copies"] <= 0:
        print("No copies available for Borrowing")
        return
    elif ISBN_no in book_db and book_db[ISBN_no]["Copies"] > 0:
        user = input("Enter User ID or Name: ")
        book_db[ISBN_no]["Copies"] -= 1
        book_db[ISBN_no]["Borrowed"] += 1
        save_data(book_db)
        print("Book_no {} is checked out successfully by user {}" .format(ISBN_no, user))
        
    

def return_book(book_db):
    ISBN_no = input("Enter the ISBN_no of book to be return : ")
    if ISBN_no not in book_db:
        print("Book is not available")
        return
    elif ISBN_no in book_db:
        user = input("Enter user ID or name: ")
        book_db[ISBN_no]["Copies"] += 1
        book_db[ISBN_no]["Borrowed"] -= 1
        save_data(book_db)
        print("Book_no {} is returned successfully by user {}" .format(ISBN_no, user))
       
