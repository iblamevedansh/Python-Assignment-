def safe_divide(numerator, denominator):
  try:
    result = numerator / denominator
    return result
  except ZeroDivisionError as e:
    print(f"Error: Cannot divide by zero. Encountered built-in exception: {e}")
    return None

numerator = 10
denominator1 = 2
denominator2 = 0

result1 = safe_divide(numerator, denominator1)
if result1 is not None:
  print(f"{numerator} / {denominator1} = {result1}")

result2 = safe_divide(numerator, denominator2)
if result2 is None:
  print(f"Division by {denominator2} failed.")