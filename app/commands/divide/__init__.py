from app.commands import Command

class DivideCommand(Command):
    def execute(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b