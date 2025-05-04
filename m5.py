import cal1

# Call the function from the imported module
operations = cal1.arithmetic_operations()

addition_result = operations["add"](5, 3)
print(f"Addition: 5 + 3 = {addition_result}")

subtraction_result = operations["subtract"](10, 4)
print(f"Subtraction: 10 - 4 = {subtraction_result}")

multiplication_result = operations["multiply"](2, 6)
print(f"Multiplication: 2 * 6 = {multiplication_result}")

division_result = operations["divide"](15, 3)
print(f"Division: 15 / 3 = {division_result}")

division_by_zero = operations["divide"](7, 0)
print(f"Division by zero: {division_by_zero}")

modulo_result = operations["modulo"](17, 5)
print(f"Modulo: 17 % 5 = {modulo_result}")

modulo_by_zero = operations["modulo"](9, 0)
print(f"Modulo by zero: {modulo_by_zero}")

power_result = operations["power"](2, 3)
print(f"Power: 2 ** 3 = {power_result}")