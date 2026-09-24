transactions=[]

# load existing data from file
def load_data():
    try:
        with open('budget.txt','r') as file:
            for line in file:
                data=line.strip().split(",")

                transaction={"type":data[0],
                             "amount":float(data[1]),
                             "category":data[2]}
                transactions.append(transaction)
    except FileNotFoundError:
        pass
# save transaction to file
def save_transaction(transaction):
    with open("budget.txt","a") as file:
        file.write(
            f"{transaction['type']},{transaction['amount']},{transaction['category']}\n"
        )

# add income
def add_income():
    amount=float(input('Enter input amount:'))
    source=input('Enter income source: ')
    transaction={
        "type": "Income",
        "amount": amount,
        "category": source
    }

    transactions.append(transaction)
    save_transaction(transaction)

    print('Income Added Successfully!\n')

# add expense
def add_expense():
    amount=float(input('Enter Expense Amount: '))
    category=input('Enter Expense Category: ')
    transaction={
        "type": "Expense",
        "amount": amount,
        "category": category
    }

    transactions.append(transaction)
    save_transaction(transaction)

    print('Expense Added Successfully!\n')

# view all transactions
def view_transactions():
    if len(transactions) == 0:
        print('No Transactions Found!\n')
        return

    print("\n----- Transactions -----")

    for i in transactions:
        print(f"{i['type']:10} {i['category']:15} {i['amount']}")
    print()

# view balance
def view_balance():
    total_income=0
    total_expense=0

    for i in transactions:

        if i["type"] == "Income":
            total_income += i["amount"]

        elif i["type"] == 'Expense':
            total_expense += i["amount"]

    balance = total_income - total_expense

    print("\n----- Balance Report -----")
    print('Total Income :',total_income)
    print('Total Expense :',total_expense)
    print('Balance       :',balance)
    print()

# expense report

def expense_report():

    report = {}

    for i in transactions:
        if i["type"] == "Expense":
            category = i["category"]

            if category in report:
                report[category] += i["amount"]
            else:
                report[category] = i["amount"]

    print("\n----- Expense Report -----")

    if len(report) == 0:
        print('No Expenses Recorded!')
    else:
        for category,amount in report.items():
            print(category, ",",amount)
        print()

# main program
load_data()
while True:

    print("----- Budget Manager -----")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4.View Balance")
    print("5.Expense Report")
    print("6. Exit")

    choice = input("Enter Choice :")

    if choice == "1":
        add_income()

    elif choice == "2":
        add_expense()

    elif choice == "3":
        view_transactions()

    elif choice == "4":
        view_balance()

    elif choice == "5":
        expense_report()

    elif choice == "6":
        print("Thank You for Using Budget Manager!")
        break

    else:
        print("Invalid Choice! Try A gain.\n")