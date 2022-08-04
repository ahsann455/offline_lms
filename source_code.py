from abc import ABC
import random
Accounts = {}
members = {}

listofbooks = {"In Search of Lost Time": "Marcel Proust",
                   "One Hundred Years of Solitude": "Gabriel Garcia Marquez",
                   "The Fault in Our Stars": "Josh Boone",
                   "Harry Potter and the Sorcerer's Stone": "J.K. Rowling",
                   "The Great Gatsby": "F. Scott Fitzgerald",
                   "War and Peace": "Leo Tolstoy", "The Odyssey": "The Homer", "The Divine Comedy": "Dante Alighieri",
                   "The Brothers Karamazov": "Fyodor Dostoyevsky", "Crime and Punishment": "Fyodor Dostoyevsky",
                   "Wuthering Heights": "Emily Bronte", "The Catcher in the Rye": "J. D. Salinger",
                   "The Adventures of Huckleberry Finn": "Mark Twain",
                   "Alice's Adventures in Wonderland": "Lewis Carroll", "To the Lighthouse": "Virginia Woolf",
                   "Heart of Darkness": "Joseph Conrad", "Nineteen Eighty Four": "Goerge Orwell",
                   "Great Expectations": "Charles Dickens", "One Thousand and One Nights": "India/Iran/Iraq/Egypt",
                   "The Grapes of Wrath": "John Steinbeck", "Invisible Man": "Ralph Ellison"
                   }

class Library():

    listofbooks = {"In Search of Lost Time": "Marcel Proust",
                   "One Hundred Years of Solitude": "Gabriel Garcia Marquez",
                   "The Fault in Our Stars": "Josh Boone",
                   "Harry Potter and the Sorcerer's Stone": "J.K. Rowling",
                   "The Great Gatsby": "F. Scott Fitzgerald",
                   "War and Peace": "Leo Tolstoy", "The Odyssey": "The Homer", "The Divine Comedy": "Dante Alighieri",
                   "The Brothers Karamazov": "Fyodor Dostoyevsky", "Crime and Punishment": "Fyodor Dostoyevsky",
                   "Wuthering Heights": "Emily Bronte", "The Catcher in the Rye": "J. D. Salinger",
                   "The Adventures of Huckleberry Finn": "Mark Twain",
                   "Alice's Adventures in Wonderland": "Lewis Carroll", "To the Lighthouse": "Virginia Woolf",
                   "Heart of Darkness": "Joseph Conrad", "Nineteen Eighty Four": "Goerge Orwell",
                   "Great Expectations": "Charles Dickens", "One Thousand and One Nights": "India/Iran/Iraq/Egypt",
                   "The Grapes of Wrath": "John Steinbeck", "Invisible Man": "Ralph Ellison"
                   }

    def Catalog(self):
        count = 0
        for books in listofbooks.keys():
            count += 1
            print("☛", count, ".", books)
        print()

    def Search(self):
        a = input('Enter the Name of the Book you want to Search: ')
        if a in listofbooks.keys():
            print(f"Yes the book {a} is available in our Library!")
            b = listofbooks.get(a)
            print(f"{a} by {b}.")
        else:
            print()
            print("Sorry the specified book is not available in our Library at the moment.")

class Student(ABC):
    def Registration(self):
        name = input("Enter your name: ")
        id = random.randint(1,10000000000)
        pw = input('Enter your password: ')
        str(id)
        members.update({name:id})
        print("You have been successfully Registered as a Member: ")
        print("Name:", name)
        print("ID:", id)

    def AccountDetails(self):
        i = input('Enter your Accounts Name: ')
        p = input("Enter your Accounts Password: ")
        Accounts.update({i: [str(id), p]})
        if p == Accounts.get(i)[-1]:
            print("Name: ",i)
            print("MEMBER ID:",members.get(i))
        else:
            print("Wrong Password.")

def main():
    student = Student()
    library = Library()
    borrowedbooklist = []
    borrowedbyusers = []

    while True:
        print()
        print("\t \t \t \t \t \t \t ———————————————————————————————————————————————————————————————")
        print("\t \t \t \t \t \t \t ——————————————————• Library Management System •———————————————— \t \t \t \t \t \t \t")
        print("\t \t \t \t \t \t \t ———————————————————————————————————————————————————————————————")
        print()
        print("★ ‖ 1. List of Available Books. ")
        print("★ ‖ 2. Request a Book.")
        print("★ ‖ 3. Return a Book.")
        print("★ ‖ 4. Search a Book.")
        print("★ ‖ 5. Look up Author of a Book.")
        print("★ ‖ 6. Register yourself as a Member")
        print("★ ‖ 7. Membership List")
        print("★ ‖ 8. Book Status")
        print("★ ‖ 9. Remove a Book")
        print("★ ‖ 10. Account Details")
        print()

        select = int(input("➥ What do you want to do: \t"))
        print()



        if select == 1:

            library.Catalog()



        elif select == 2:

            name = input("Enter your name: ")
            ID = input("Your Membership ID: ")
            for member in members.keys():
                if member == name:
                    for key, value in members.items():
                        if str(ID) == str(value):
                            book = input("Enter the name of the book you want to borrow: ")
                            listofbooks.pop(book)
                            print("You have borrowed the book", book)
                            break
                else:
                    print("Sorry you are not a registered Member.")
                    print("Please register first!")
                    break



        elif select == 3:

            name = input('Enter your name: ')
            z = input("Enter the name of the Book you want to return: ")

            listofbooks.update({z:listofbooks.get(book)})
            borrowedbooklist.remove(z)
            borrowedbyusers.remove(name)


            print("You have returned the book",z)


        elif select == 4:

            library.Search()


        elif select == 5:

            i = input("Enter the name of the book you want to find the Author of: ")

            listofbooks.get(i)

            print("The author of the book "f"{i} is",listofbooks.get(i))


        elif select == 6:

            student.Registration()


        elif select == 7:

            pw = input("Input the administrator Password: ")
            if pw == "ahsan123":
                print(members)
            else:
                print('Wrong Password')


        elif select == 8:

            pw = input("Input the administrator Password: ")
            if pw == "ahsan123":

                y = len(borrowedbooklist)
                if y == 0:
                    print('No books have been borrowed.')

                elif y>0:
                    print(borrowedbooklist)
                    print("Borrowed By")
                    print(borrowedbyusers)
            else:
                print("Wrong Password.")

        elif select == 9:

            pw = input("Input the administrator Password: ")
            if pw == "ahsan123":
                dele = input('Enter the name of the book you want to remove: ')
                print(dele)
                listofbooks.pop(dele)
                print("The Book",dele,"Was Successfully removed!")
            else:
                print("Wrong Password.")

        elif select == 10:
            student.AccountDetails()

main()
