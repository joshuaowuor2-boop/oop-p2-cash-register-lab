# Cash Register (OOP Part 2)

A Python `CashRegister` class that models a simple point-of-sale register for
an e-commerce site: add items, apply a percentage discount to the running
total, and void the most recently added transaction.

## Description

`CashRegister` (defined in [lib/cash_register.py](lib/cash_register.py)) tracks:

* `discount` — a whole-number percentage (0-100) taken off the total when
  `apply_discount()` is called. Defaults to `0` if not provided, or if an
  invalid value (non-integer, or outside 0-100) is supplied, in which case
  `"Not valid discount"` is printed.
* `total` — the running dollar total of all items added, minus any applied
  discount. Starts at `0`.
* `items` — a flat list of every item name added so far (an item added with
  a quantity of 3 appears 3 times).
* `previous_transactions` — a list of dicts (`{"item", "price", "quantity"}`)
  recording each call to `add_item`, most recent last.

### Methods

* `add_item(item, price, quantity=1)` — adds `price * quantity` to `total`,
  appends `item` to `items` (`quantity` times), and records the transaction.
* `apply_discount()` — reduces `total` by `discount` percent and prints
  `"After the discount, the total comes to $<total>."`. If `discount` is `0`,
  prints `"There is no discount to apply."` instead.
* `void_last_transaction()` — reverses the most recent `add_item` call,
  removing its items from `items` and subtracting its price from `total`.
  If there are no transactions to undo, prints
  `"There is no transaction to void."`.

## Usage

```python
from cash_register import CashRegister

register = CashRegister(discount=20)
register.add_item("book", 15.00, 2)   # total -> 30.0
register.apply_discount()             # -> "After the discount, the total comes to $24."
register.void_last_transaction()      # undoes the "book" transaction
```

## Installation

This project uses [Pipenv](https://pipenv.pypa.io/) to manage dependencies.

```console
pipenv install
pipenv shell
```

## Testing

Tests are written with `pytest` and live in `lib/testing/`:

```console
pytest
```

## Tools & Resources

* [Python Classes](https://docs.python.org/3/tutorial/classes.html)

## License

See [LICENSE.md](LICENSE.md).
