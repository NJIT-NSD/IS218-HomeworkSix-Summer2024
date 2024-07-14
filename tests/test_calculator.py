'''My Calculator Test'''
from calculator.calculator_section import Calculations
from faker import Faker
from decimal import Decimal
import pytest

fake = Faker()

def generate_test_data(num_records):
    # Define operation mappings for both Calculator and Calculation tests
    operation_mappings = {
        'add': Calculations.addition,
        'subtract': Calculations.subtraction,
        'multiply': Calculations.multiplication,
        'divide': Calculations.division
    }
    # Generate test data
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        
        # Ensure b is not zero for divide operation to prevent division by zero in expected calculation
        if operation_func == Calculations.division:
            b = Decimal('1') if b == Decimal('0') else b
        
        try:
            if operation_func == Calculations.division and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        print("function ran")
        # yield a, b, operation_name, operation_func, expected

@pytest.fixture
def single_number_faker():
    return Decimal(Faker().random_number(digits=2))

def test_addTwoNumbers(single_number_faker):
    a = single_number_faker
    b = single_number_faker
    expected = a + b
    assert Calculations.addition(a, b) == expected

def test_subtractTwoNumbers(single_number_faker):
    a = single_number_faker
    b = single_number_faker
    expected = a - b
    assert Calculations.subtraction(a, b) == expected

def test_multiplyTwoNumbers(single_number_faker):
    a = single_number_faker
    b = single_number_faker
    expected = a * b
    assert Calculations.multiplication(a, b) == expected

def test_divideTwoNumbers(single_number_faker):
    a = single_number_faker
    b = single_number_faker
    expected = a / b
    assert Calculations.division(a, b) == expected

def test_addition():
    '''Test that addition function works '''    
    assert Calculations.addition(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works '''    
    assert Calculations.subtraction(2,2) == 0

def test_multiplication():
    '''Test that multplication function works '''
    assert Calculations.multiplication(3,3) == 9

def test_division():
    '''Test that division function works '''
    assert Calculations.division(9, 3) == 3