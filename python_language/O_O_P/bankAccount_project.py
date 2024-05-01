#!/usr/bin/python3

from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(1000)

Dave.withdraw(50000)
Dave.withdraw(100)
