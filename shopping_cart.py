""" Flatiron Data Science OOP shopping cart lab."""
import numpy as np

class ShoppingCart:
    """Shopping cart. Optional parameter: emp_discount percentage greater than 0 and less than 100."""
    # write your code here

    def __init__(self, emp_discount: float=None):
        self.total = 0
        emp_discount = self._validate_emp_discount(emp_discount)
        self.employee_discount = emp_discount
        self.items = []
        self.discount_applied = False

    def _validate_emp_discount(self, emp_discount: float):
        """Ensures employee discount is greater than 0 and less than 100."""
        if (emp_discount is not None) and ((emp_discount >= 100) or (emp_discount <= 0)):
            print("Employee discount must be a percentage greater than zero and less than 100.")
            return None
        else:
            return emp_discount

    def _validate_quantity(self, quantity: int):
        """Ensures quantity of item is a positive integer."""
        if quantity < 1:
            print("Quantity must be a positive integer.")
            return 1
        else:
            return quantity

    def add_item(self, name: str, price: float, quantity: int=1):
        """Add item with name, price, and quantity (default 1)."""
        item = Item(name, price)
        quantity = self._validate_quantity(quantity)
        items = [item] * quantity
        self.items.extend(items)
        if self.discount_applied:
            self.remove_discount()
        self.total += price * quantity
        return self.total

    def mean_item_price(self) -> float:
        """Return the average price per item of the cart."""
        return np.average([item.price for item in self.items])

    def median_item_price(self) -> float:
        """Return the median price per item of the cart."""
        return np.median([item.price for item in self.items])

    def apply_discount(self):
        """Apply employee discount to total. Can only be applied once
        and is removed if the cart is changed."""
        if not self.employee_discount:
            return "Sorry, there is no discount to apply to your cart :("
        elif not self.discount_applied:
            self.total = self.total * (100 - self.employee_discount) / 100
            self.discount_applied = True
            return self.total
        else:
            return "Sorry, discount already applied."

    def remove_discount(self):
        """Remove employee discount from total."""
        if self.discount_applied:
            self.total = self.total / (100 - self.employee_discount) * 100
            self.discount_applied = False

    def void_last_item(self):
        """Remove last item added to the cart. If that item's quantity was
        greater than one, reduces quantity by one. Removes employee discount
        if previously applied."""
        if not self.items:
            return "There are no items in your cart!"
        else:
            item_removed = self.items.pop()
            if self.discount_applied:
                self.remove_discount()
            self.total -= item_removed.price
            return self.total

class Item:
    """Item class."""

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}: ${self.price:,.2f}"
