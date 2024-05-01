#!/usr/bin/python3

class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created.\nBalance = $'{self.balance:.2f}'")
