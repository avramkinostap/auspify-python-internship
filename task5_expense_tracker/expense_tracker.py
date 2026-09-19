import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"


def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date = datetime.now().strftime("%Y-%m-%d")

    file_exists = os.path.exists(FILENAME)

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Category", "Amount"])
        writer.writerow([date, category, amount])

    print("Expense added.")


def show_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses recorded yet.")
        return

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            date, category, amount = row
            print(f"{date} | {category} | {amount}")


def show_summary():
    if not os.path.exists(FILENAME):
        print("No expenses recorded yet.")
        return

    monthly_totals = {}
    category_totals = {}

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            date, category, amount = row
            amount = float(amount)
            month = date[:7]

            monthly_totals[month] = monthly_totals.get(month, 0) + amount
            category_totals[category] = category_totals.get(category, 0) + amount

    print("\nMonthly Totals")
    for month, total in monthly_totals.items():
        print(f"{month}: {total:.2f}")

    print("\nCategory Totals")
    for category, total in category_totals.items():
        print(f"{category}: {total:.2f}")


def show_menu():
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. Show all expenses")
    print("3. Show monthly summary")
    print("4. Clear all expenses")
    print("5. Exit")


def clear_expenses():
    confirm = input("Are you sure you want to delete all expenses? (y/n): ")
    if confirm.lower() == "y":
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
            print("All expenses cleared.")
        else:
            print("No expenses to clear.")
    else:
        print("Cancelled.")



while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        clear_expenses()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")