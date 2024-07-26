from app.commands import Command
from decimal import Decimal, InvalidOperation

class DivideCommand(Command):
    def execute(self, a, b):
        try:
            a = Decimal(a)
            b = Decimal(b)
            result = a / b
            print(f"The result of {a} / {b} is {result}")
        except ZeroDivisionError:
            print(f"Cannot divide by zero.")
        except InvalidOperation:
            print(f"Invalid number input: {a} or {b} is not a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")