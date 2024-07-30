import sys
from decimal import Decimal, InvalidOperation
from calculator import calculator_section
from app import App
import logging
import logging.config

# Configure logging
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger.info("Logging setup complete.")

class OperationCommand:
    def __init__(self, calculator, operation_name, a, b):
        self.calculator = calculator
        self.operation_name = operation_name
        self.a = a
        self.b = b

    def execute(self):
        logger = logging.getLogger(__name__)
        logger.info(f"Executing command: {self.operation_name} with arguments: {self.a}, {self.b}")
        operation_method = getattr(self.calculator, self.operation_name, None)
        if operation_method:
            try:
                return operation_method(self.a, self.b)
            except Exception as e:
                logger.error(f"Error during operation execution: {e}")
                raise
        else:
            raise ValueError(f"Unknown operation: {self.operation_name}")

def calculate_and_print(a, b, operation_name):
    logger = logging.getLogger(__name__)
    logger.info(f"Calculating: {a} {operation_name} {b}")
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        command = OperationCommand(calculator_section, operation_name, a_decimal, b_decimal)
        result = command.execute()
        logger.info(f"The result of {a} {operation_name} {b} is equal to {result}")
        print(f"The result of {a} {operation_name} {b} is equal to {result}")
    except InvalidOperation:
        logger.error(f"Invalid number input: {a} or {b} is not a valid number.")
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        logger.error("Error: Division by zero.")
        print("Error: Division by zero.")
    except ValueError as e:
        logger.error(f"ValueError: {e}")
        print(f"ValueError: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

def main():
    logger = logging.getLogger(__name__)
    logger.info("Main function started.")
    if len(sys.argv) != 4:
        logger.error("Usage: python main.py <number1> <number2> <operation>")
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation_name = sys.argv
    calculate_and_print(a, b, operation_name)
    logger.info("Main function finished.")

if __name__ == '__main__':
    logger.info("Program started.")
    if len(sys.argv) == 1:
        app = App()
        app.start()
    else:
        main()
    logger.info("Program finished.")


    '''import sys
    from decimal import Decimal, InvalidOperation
    from calculator import calculator_section 
    from app import App
    import logging
    import logging.config

    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger(__name__)
    logger.info("Logging setup complete.")

    class OperationCommand:
        def __init__(self, calculator, operation_name, a, b):
            self.calculator = calculator
            self.operation_name = operation_name
            self.a = a
            self.b = b

        def execute(self):
            logger = logging.getLogger(__name__)
            logger.info(f"Executing command: {self.operation_name} with arguments: {self.a}, {self.b}")
            # Retrieve the operation method from the Calculator class using getattr
            operation_method = getattr(self.calculator, self.operation_name, None)
            if operation_method:
                return operation_method(self.a, self.b)
            else:
                raise ValueError(f"Unknown operation: {self.operation_name}")

    def calculate_and_print(a, b, operation_name):
        logger = logging.getLogger(__name__)
        logger.info(f"Calculating: {a} {operation_name} {b}")
        print(a, b)
        try:
            a_decimal, b_decimal = map(Decimal, [a, b])
            command = OperationCommand(calculator_section, operation_name, a_decimal, b_decimal)
            result = command.execute()
            logger.info(f"The result of {a} {operation_name} {b} is equal to {result}")
            print(f"The result of {a} {operation_name} {b} is equal to {result}")
        except InvalidOperation:
            logger.error(f"Invalid number input: {a} or {b} is not a valid number.")
            print(f"Invalid number input: {a} or {b} is not a valid number.")
        except ZeroDivisionError:
            logger.error("Error: Division by zero.")
            print("Error: Division by zero.")
        except ValueError as e:
            logger.error(e)
            print(e)
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            print(f"An error occurred: {e}")

    def main():
        logger = logging.getLogger(__name__)
        logger.info("Main function started.")
        if len(sys.argv) != 4:
            logger.error("Usage: python main.py <number1> <number2> <operation>")
            print("Usage: python main.py <number1> <number2> <operation>")
            sys.exit(1)

        _, a, b, operation_name = sys.argv
        calculate_and_print(a, b, operation_name)
        logger.info("Main function finished.")

    if __name__ == '__main__':
        if len(sys.argv) == 1:
            logger.info("Program started.")
            app = App()
            app.start()
            logger.info("App finished.")
        else:
            main()
        logger.info("Program finished.")

    '''