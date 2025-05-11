import json
import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    """Loads expenses from the JSON file."""
    try:
        with open(DATA_FILE, "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []
    return expenses

def save_expenses(expenses):
    """Saves expenses to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    """Adds a new expense."""
    amount_str = input("Enter the expense amount: ")
    try:
        amount = float(amount_str)
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    description = input("Enter a brief description: ")
    category = input("Enter the category (e.g., food, travel, bills): ")
    date_str = input("Enter the date (YYYY-MM-DD, leave blank for today): ")
    if date_str:
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Using today's date.")
            date = datetime.date.today()
    else:
        date = datetime.date.today()

    new_expense = {
        "amount": amount,
        "description": description,
        "category": category,
        "date": date.isoformat()
    }
    expenses.append(new_expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses(expenses):
    """Displays all recorded expenses."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for i, expense in enumerate(expenses):
        print(f"{i+1}. Amount: {expense['amount']:.2f}, Description: {expense['description']}, "
              f"Category: {expense['category']}, Date: {expense['date']}")
    print("--------------------")

def filter_expenses_by_category(expenses):
    """Filters expenses by a specified category."""
    category = input("Enter the category to filter by: ")
    filtered_expenses = [exp for exp in expenses if exp['category'].lower() == category.lower()]

    if not filtered_expenses:
        print(f"No expenses found in the category '{category}'.")
        return

    print(f"\n--- Expenses in '{category}' ---")
    for i, expense in enumerate(filtered_expenses):
        print(f"{i+1}. Amount: {expense['amount']:.2f}, Description: {expense['description']}, "
              f"Date: {expense['date']}")
    print("----------------------------")

def filter_expenses_by_date_range(expenses):
    """Filters expenses within a specified date range."""
    start_date_str = input("Enter the start date (YYYY-MM-DD): ")
    end_date_str = input("Enter the end date (YYYY-MM-DD): ")

    try:
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format.")
        return

    filtered_expenses = [
        exp for exp in expenses
        if start_date <= datetime.datetime.strptime(exp['date'], "%Y-%m-%d").date() <= end_date
    ]

    if not filtered_expenses:
        print(f"No expenses found between {start_date} and {end_date}.")
        return

    print(f"\n--- Expenses between {start_date} and {end_date} ---")
    for i, expense in enumerate(filtered_expenses):
        print(f"{i+1}. Amount: {expense['amount']:.2f}, Description: {expense['description']}, "
              f"Category: {expense['category']}, Date: {expense['date']}")
    print("---------------------------------------------------")

def main():
    """Main function to run the expense tracker app."""
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Filter by Date Range")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            filter_expenses_by_category(expenses)
        elif choice == '4':
            filter_expenses_by_date_range(expenses)
        elif choice == '5':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
  
