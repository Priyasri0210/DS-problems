from tracker import *

#Display the menu options

def display_menu():
    print("==============Expense Tracker=================")
    print("Enter the option number only")
    print("1. Add new Expenses")
    print("2. View all expenses")
    print("3. Add new category")
    print("4. Delete Expenses")
    print("5. filter by category")
    print("6. Month statistics")
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
        elif choice == 5:
            filter_by_category()
        elif choice == 6:
            count_by_month()
        elif choice == 7:
            break
        else:
            print('Invalid input')


if __name__ == '__main__':
    main()