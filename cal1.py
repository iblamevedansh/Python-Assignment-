def arithmetic_operations():

    def add1(x, y):
        #Adds two numbers.
        return x + y

    def sub1(x, y):
        #Subtracts the second number from the first.
        return x - y

    def mul1(x, y):
        #Multiplies two numbers.
        return x * y

    def div1(x, y):
        #Divides the first number by the second. Handles division by zero.
        if y == 0:
            return 
        return x / y

    def mod1(x, y):
        #Returns the remainder of the division of the first number by the second.
        if y == 0:
            return 
        return x % y

    def pow1(x, y):
        #Raises the first number to the power of the second.
        return x ** y

    return {
        "add": add1,
        "subtract": sub1,
        "multiply": mul1,
        "divide": div1,
        "modulo": mod1,
        "power": pow1,
    }

