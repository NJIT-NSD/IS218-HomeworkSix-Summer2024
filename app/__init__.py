from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.menu import MenuCommand

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        # Register commands here
        #self.command_handler.register_command("greet", GreetCommand())
        #self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            # parsed_string = self.command_parser(input(">>> ").strip())
            self.command_handler.execute_command(input(">>> ").strip())

    def command_parser(self, input_string: str):
        args_array = input_string.split()
        dict = {
            "command": args_array[0],
            "variable_one": args_array[1],
            "variable_two": args_array[2]
        }