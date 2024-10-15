import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        date = datetime.date.today()
        self.expenses.append({"date": date, "amount": amount, "category": category})
        print(f"Expense added: ${amount:.2f} for {category}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            for expense in self.expenses:
                print(f"{expense['date']} - ${expense['amount']:.2f} - {expense['category']}")

    def get_summary(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            total = sum(expense['amount'] for expense in self.expenses)
            categories = {}
            for expense in self.expenses:
                if expense['category'] in categories:
                    categories[expense['category']] += expense['amount']
                else:
                    categories[expense['category']] = expense['amount']
            
            print(f"\nTotal expenses: ${total:.2f}")
            print("\nExpenses by category:")
            for category, amount in categories.items():
                print(f"{category}: ${amount:.2f}")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. View expense summary")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            amount = float(input("Enter expense amount: $"))
            category = input("Enter expense category: ")
            tracker.add_expense(amount, category)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.get_summary()
        elif choice == '4':
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
