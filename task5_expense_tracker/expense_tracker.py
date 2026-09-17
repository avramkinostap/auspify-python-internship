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

add_expense()