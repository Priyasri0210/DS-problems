from tracker import *

#Display the menu options

def display_menu():
    print("==============Expense Tracker=================")
    print("Enter the option number only")
    print("1. Add new Expenses")
    print("2. View all expenses")
    print("3. Add new category")
    print("4. Delete Expenses")
    # print("5. View Students")
    # print("6. Course Statistics")
    print("7. Exit")


def main():
    while True:
        display_menu()
        choice = int(input("Enter the choice : "))

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            add_category()
        elif choice == 4:
            delete_expense()
        # elif choice == 5:
        #     view_students(students_db)
        # elif choice == 6:
        #     course_statistics(students_db)
        elif choice == 7:
            break
        else:
            print('Invalid input')


if __name__ == '__main__':
    main()