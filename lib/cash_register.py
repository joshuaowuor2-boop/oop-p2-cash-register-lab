#!/usr/bin/env python3


class CashRegister:
    """Simulates a cash register for an e-commerce site.

    Supports adding items, applying a percentage discount to the
    running total, and voiding the most recent transaction.
    """

    def __init__(self, discount=0):
        # discount is validated/normalized through the property setter below.
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        # discount must be a whole-number percentage between 0 and 100.
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")
            self._discount = 0

    @staticmethod
    def _format_amount(amount):
        # Drops a trailing ".0" (e.g. 800.0 -> "800") while still showing
        # cents when the amount actually has them (e.g. 84.99 -> "84.99").
        if amount == int(amount):
            return str(int(amount))
        return str(round(amount, 2))

    def add_item(self, item, price, quantity=1):
        """Add an item (or multiple of the same item) to the register."""
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        """Apply the register's discount percentage to the current total."""
        if not self.discount:
            print("There is no discount to apply.")
            return

        self.total -= self.total * (self.discount / 100)
        print(f"After the discount, the total comes to ${self._format_amount(self.total)}.")

    def void_last_transaction(self):
        """Undo the most recent add_item transaction."""
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        for _ in range(last_transaction["quantity"]):
            self.items.remove(last_transaction["item"])
