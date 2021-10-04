## ID= 336677 , Password = boss@123
from databook import booksltss
from difflib import get_close_matches
import string
data = booksltss
display_available_book = booksltss.copy()

lendDict = {}
issued_books = {}

def all_book():
    print("\nWe have following books in our library: \n")
    booksltss
    for bookname in booksltss:
        print(string.capwords(bookname))

def available_book():
    print("\nCurrently Available books in the library: ")
    for bookname in display_available_book:
        print(string.capwords(bookname))
        
def lend_book(user ,book ):
    if book not in lendDict.keys():        
        if book in display_available_book:
            lendDict.update({book:user})
            print("Lenders book data has been updated. You can take the book now!")
            issued_books.update({book:user})
            display_available_book.pop(book)
        else:
            print("invalid , Please enter the correct name of the book ")
    else:
        print(f"Sorry! This book is alredy being used by {lendDict[book]} ")

def add_book(book, discription):
    booksltss.update({book:discription})
    display_available_book.update({book:discription})
    print("New book has been added to the book list")

def get_meaning(book):   
    if book in data:
        if len(data[book]) > 1:
            for i in data[book]:
                print(i)
    else:
        close_match = get_close_matches(book, data.keys())
        if len(close_match) > 0:
            print("finding the closest match to this is : ", close_match)
            print("\n",close_match[0],"\nDescription : ",end=" " )
            for i in data[close_match[0]]:
                print(i ,end="" )
        else:
            print("There is no book related to it, Can't found the Book! ")

def return_book():
    book = input("\nEnter the name of book you want to Return: ").lower()
    if book in lendDict.keys():
        lendDict.pop(book)
        print("Your book has been returned")
        issued_books.pop(book)
        display_available_book[book]=[data[book]]
    else:
        print("\nDid not find the similar book in the lend books")
        get_meaning(book)
        print("\nPlease enter book name correctly")
        return_book()

def delete_book():
    book = input("\nEnter book name you want to delete book: ")
    if book in booksltss.keys():
        booksltss.pop(book)
        display_available_book.pop(book)
        print("\nBook has been successfully deleted")
    else:
        print("\nDid not find the similar book in the books")
        get_meaning(book)
        print("\nPlease enter book name correctly")
        


if __name__ == '__main__':
    while (True):
        print("\nWelcome to the library.\n")
        print("Choose the task you want to perform!")
        print("Enter\n1 Display All the books in the library \n2 Display Currently Available books \n3 Search book \n4 Lend Book \n5 Add a book \n6 Return book \n7 view lend details(For Authorised Person Only) \n8 Delete Book\n")
        task = input("Enter your choice: ")
        
        if task == "1":
            all_book()
        
        elif task == "2":
            available_book()

        elif task == "3":
            print("\nSearch books :")
            book = input("Please enter the book you searching for: ").lower()
            get_meaning(book)
        
        elif task == "4":
            user = input("\nEnter your name: ")
            book = input("Enter the name of the book you want to Lend: ")
            lend_book(user, book)

        elif task == "5":
            book = input("\nEnter the name and author of book you want to Add: ")
            discription = input("Please enter a brief description of the book here: ")
            add_book(book, discription)
        
        elif task == "6":
            # author = input("Author name")
            return_book()

        elif task == "7":
            a = input("\nEnter User ID : ")
            b = input("Enter the Password : ")
            if a == '336677' and b == 'boss@123':
                if len(issued_books)>0:
                    print("\nBook issued to ")
                    for i in issued_books:
                        print(i," : ",issued_books[i]) 
                else:
                    print("NO issued book")
            else:
                print('Invalid ID or Password')
        
        elif task == "8":
            delete_book()
        
        else:
            print("Not a valid option")
        


        y_n = ""
        while (y_n != "Y" and y_n != "N"):
            y_n = input("\n Press 'Y' to Continue or 'N' to exit ").upper()
            if y_n == "Y":
                continue
            elif y_n == "N":
                print("Thank You ! for using our service")
                exit()
