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

    def execute_command(self, input_string: str):
        parsed_command = command_parser(input_string)
        command_name = parsed_command['command']
        args = parsed_command.get('args', [])

        try:
            self.commands[command_name].execute(*args)
        except KeyError:
            print(f"No such command: {command_name}")
        except TypeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
def command_parser(input_string: str):
    args_array = input_string.split()
    if len(args_array) == 1:
        return {"command": args_array[0], "args": []}
    return {
        "command": args_array[0],
        "args": args_array[1:]
    }
    
    