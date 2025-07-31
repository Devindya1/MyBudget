import db
from datetime import datetime

def show_menu():
    print("\n=== My Budget menu ===")
    print("1. Add category")
    print("2. Add expense")
    print("3. Show expenses")
    print("4. Show summery by category")
    print("5. Exit")

def add_category():
    name = input("Enter new category name: ").strip()
    if not name:
        print("Category name cannot be empty.")
        return
    if db.add_category(name):
        print(f"Category '{name}' added successfully.")

def add_expense():
    categories = db.get_categories()
    if not categories:
        print("No categories available. Please add a category first.")
        return
    print("\nCategories:")
    for cat_id,cat_name in categories:
        print(f"{cat_id}. {cat_name}")
    try:
        category_id = int(input("Enter your Category ID:"))
        if category_id not in [cat[0] for cat in categories]:
            print("Invalid category ID: Please try again.")
            return    
        description = input("Enter expense description: ").strip()
        amount = float(input("Enter expense amount: "))
        data_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
        expense_date = datetime.strptime(data_str, "%Y-%m-%d").date()
        db.add_expense(category_id, description, amount, expense_date)
        print("Expense added successfully.")
    except ValueError:
        print("Invalid input. Please enter correct data types.")
    except Exception as e:
        print(f"error: {e}")

def view_expenses():
    expenses = db.get_expenses()
    if not expenses:
        print("No expenses found.")
        return
    print("\n=== Expenses ===")
    for exp_id,cat_name,desc,amount,date in expenses:
        print(f"ID: {exp_id}, Category: {cat_name}, Description: {desc}, Amount: RS.{amount:.2f}, Date: {date}")

def view_summary():
    summary = db.get_summary()
    if not summary:
        print("No expenses found.")
        return
    print("\n=== Summary by Category ===")
    for cat_name, total in summary:
        print(f"Category: {cat_name}, Total: RS.{total:.2f}")


def main():
    while True:
        show_menu()
        choice = input("Enter your option (1-5): ").strip()
        if choice == '1':
            add_category()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            view_expenses()
        elif choice == '4':
            view_summary()
        elif choice == '5':
            print("Exiting Mybudget. Goodbye! Have a nice day!")
            break    
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()