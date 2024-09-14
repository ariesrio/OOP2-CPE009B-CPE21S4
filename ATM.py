"""
    ATM.py
"""

class ATM():
  def __init__(self, serial_number=0):
      self.serial_number = serial_number
      self.transactions = []

  def deposit(self, account, amount):
    account.current_balance = account.current_balance + amount
    self.transactions.append(f"Deposit of {amount} to account {account.account_number}")
    print("Deposit Complete")

  def withdraw(self, account, amount):
    if amount <= account.current_balance:
        account.current_balance = account.current_balance - amount
        self.transactions.append(f"Withrawal of {amount} from account {account.account_number}")
        print("Withdraw Complete")
    else:
       print("Insufficient Balance")

  def check_currentbalance(self, account):
      print(f"Current Balance: {account.current_balance}")

  def view_transactionsummary(self):
      print(f"Transaction Summary:{self.transactions}")
      
