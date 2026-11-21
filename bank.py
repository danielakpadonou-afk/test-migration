# -*- coding: utf-8 -*-
"""Mini application bancaire (Python 2)."""
import sys


class InsufficientFunds(Exception):
    pass


class Account(object):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __bool__(self):
        return self.balance != 0

    def __cmp__(self, other):
        return cmp(self.balance, other.balance)

    def __unicode__(self):
        return "%s: %d" % (self.owner, self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("solde insuffisant")
        self.balance -= amount

    def monthly_interest(self):
        return self.balance * 3 / 100


def transfer(src, dst, amount):
    try:
        src.withdraw(amount)
    except InsufficientFunds as e:
        print("Erreur :", e, file=sys.stderr)
        return False
    dst.balance += amount
    return True


def debug(obj):
    return repr(obj)


def run(code):
    exec(code)


def main():
    a = Account("Ali", 1000)
    b = Account("Sara")
    print(transfer(a, b, 300))
    print(a.monthly_interest(), debug(b.balance))
    print(a > b)


main()
