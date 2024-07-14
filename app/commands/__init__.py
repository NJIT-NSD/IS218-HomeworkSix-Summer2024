from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        try:
            command_parser(command_name)
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
    
def command_parser(input_string: str):
    args_array = input_string.split()
    print(args_array)
    if len(args_array) == 1:
        return args_array[0]
    return {
        "command": args_array[0],
        "variable_one": args_array[1],
        "variable_two": args_array[2]
    }
    
    '''def handle_user_input(self):
        while True:
            user_input = input("Enter command (add/subtract): ")
            if user_input.lower() == "exit":
                break
            
            parts = user_input.split()
            if len(parts) < 3:
                print("Invalid command format. Example: add 5 3")
                continue
            
            command_name = parts[0].lower()
            operands = [float(parts[1]), float(parts[2])]

            self.execute_command(command_name, operands)'''