import data

def check_balance():
    return data.balance

def deposit(amount):
    if amount <= 0:
        return "Invalid"
    data.balance = data.balance + amount
    data.transactions.append("Deposited " + str(amount))
    return "Done"

def withdraw(amount):
    if amount <= 0:
        return "Invalid"
    if amount > data.balance:
        return "Not enough balance"
    data.balance = data.balance - amount
    data.transactions.append("Withdrawn " + str(amount))
    return "Done"

def show_transactions():
    return data.transactions