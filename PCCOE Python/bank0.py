
balance = 0

def get_balance():
    return balance

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    balance -= amount
if __name__ == "__main__":
    pass