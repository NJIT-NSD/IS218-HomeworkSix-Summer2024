import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
import logging

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()
        self.logger = logging.getLogger(__name__)
        self.logger.info("App initialized.")

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        self.logger.info("Loading plugins...")
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore
    def start(self):
        # Register commands here
        self.logger.info("App started.")
        self.load_plugins()
        print("Type 'exit' to exit.")
        while True:
            try:
                user_input = input(">>> ").strip()
                self.logger.info(f"User input: {user_input}")
                if user_input == 'exit':
                    print("Exiting...")
                    raise SystemExit
                self.command_handler.execute_command(user_input)
            except SystemExit:
                break
            except Exception as e:
                self.logger.error(f"Error executing command: {e}")
                print(f"Error: {e}")

    

    '''import pkgutil
    import importlib
    from app.commands import CommandHandler
    from app.commands import Command
    import logging

    class App:
        def __init__(self): # Constructor
            self.command_handler = CommandHandler()
            self.logger = logging.getLogger(__name__)
            self.logger.info("App initialized.")

        def load_plugins(self):
            # Dynamically load all plugins in the plugins directory
            self.logger.info("Loading plugins...")
            plugins_package = 'app.plugins'
            for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
                if is_pkg:  # Ensure it's a package
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    for item_name in dir(plugin_module):
                        item = getattr(plugin_module, item_name)
                        try:
                            if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                                self.command_handler.register_command(plugin_name, item())
                        except TypeError:
                            continue  # If item is not a class or unrelated class, just ignore
        def start(self):
            # Register commands here
            self.logger.info("App started.")
            self.load_plugins()
            print("Type 'exit' to exit.")
            while True:  # REPL Read, Evaluate, Print, Loop
                try:
                    user_input = input(">>> ").strip()
                    self.logger.info(f"User input: {user_input}")
                    self.command_handler.execute_command(user_input)
                except SystemExit:
                    break
                except Exception as e:
                    self.logger.error(f"Error executing command: {e}")
                    print(f"Error: {e}")



    from app.commands import CommandHandler
    'from app.commands.exit import ExitCommand'
    from app.commands.add import AddCommand
    from app.commands.subtract import SubtractCommand
    from app.commands.multiply import MultiplyCommand
    from app.commands.divide import DivideCommand
    'from app.commands.menu import MenuCommand'

    class App:
        def __init__(self): # Constructor
            self.command_handler = CommandHandler()

        def start(self):
            # Register commands here
            #self.command_handler.register_command("greet", GreetCommand())
            #self.command_handler.register_command("goodbye", GoodbyeCommand())
            #self.command_handler.register_command("exit", ExitCommand())
            #self.command_handler.register_command("menu", MenuCommand())
            self.command_handler.register_command("add", AddCommand())
            self.command_handler.register_command("subtract", SubtractCommand())
            self.command_handler.register_command("multiply", MultiplyCommand())
            self.command_handler.register_command("divide", DivideCommand())

            print("Type 'exit' to exit.")
            while True:  #REPL Read, Evaluate, Print, Loop
                user_input = input(">>> ").strip()
                self.command_handler.execute_command(user_input)'''
