from app.commands import Command

class AddCommand(Command):
    def execute(self, a, b):
        return a + b

'''class AddCommand(Command):
    def __init__(self, receiver, operand1, operand2):
        self.receiver = receiver
        self.operand1 = operand1
        self.operand2 = operand2

    def execute(self):
        return self.receiver.add(self.operand1, self.operand2)'''

'''class AddCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver
        self.operands = None

    def execute(self):
        if self.operands:
            return self.receiver.addition(*self.operands)
        else:
            raise ValueError("Operands not set")

    def set_operands(self, operands):
        self.operands = operands'''
