def add(x, y):
    """
    Add two numbers together
    """
    return x + y

def subtract(x, y):
    """
    Subtract two numbers
    """
    return x - y

def multiply(x, y):
    """
    Multiply two numbers
    """
    return x * y

def divide(x, y):
    """
    Divide two numbers
    """
    return x / y

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    """
    Calculate the sum, product, and quotient of two numbers
    """
    print("Please select an operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        try:
            user_input = input("Enter an operation: ")
            if user_input in operations:
                num_1 = float(input("Enter the first number: "))
                num_2 = float(input("Enter the second number: "))
                calculation = operations[user_input]
                answer = calculation(num_1, num_2)
                print(f"{num_1} {user_input} {num_2} = {answer}")
            else:
                print("Invalid operation")
        except ValueError:
            print("Invalid input")
        except KeyError:
            print("Invalid input")
        except Exception as e:
            print(e)
        finally:
            print("Press enter to continue...")
            input()

calculator()