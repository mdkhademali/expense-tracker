def display_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Calculate total expenses")
    print("4. Exit")

def add_expense(expenses):
    try:
        name = input("Enter expense name: ").strip()
        amount = float(input("Enter expense amount: "))
        expenses.append({"name": name, "amount": amount})
        print(f"Expense '{name}' of amount {amount:.2f} added successfully.")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nYour Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['name']} - ${expense['amount']:.2f}")

def calculate_total(expenses):
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")

def main():
    expenses = []
    print("Welcome to Basic Expense Tracker!")
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()