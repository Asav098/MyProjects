import json
import os
import datetime
def clear_expenses():
        global expenses
        expenses.clear()
        save_expenses()
        print("Expenses has been cleared")
def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json","r") as f:
            return json.load(f)
    return []
def save_expenses():
        with open("expenses.json","w") as f:
            json.dump(expenses, f)
def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date = str(datetime.date.today())

    expense = {
        "category" : category,
        "amount" : amount,
        "date" : date
    }
    expenses.append(expense)
    save_expenses()
    print("Expenses added!")
def view_expenses():
    
    for expense in expenses:
        date = expense.get("date", "No date")
        print(f"{date} - {expense['category']} - {expense['amount']}")
def view_total():
    total = 0
   
    for expense in expenses:
        total += expense["amount"]
    print(f"Total spent - {total}")
expenses = load_expenses() 
while True:
    print("\n" + "="*30)
    print("Choose an option: (1,2,3,4,5)")
    print("1. Add expenses")   
    print("2. View expenses")
    print("3. Total expenses")
    print("4. Clear all expenses")
    print("5. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_total()
    elif choice == "4":
        clear_expenses()
    elif choice == "5":
        break
    else:    
        print("Enter a valid answer")