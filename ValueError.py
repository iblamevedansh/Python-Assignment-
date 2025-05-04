def process_value(value):
    
  try:
    # Example processing that might raise a ValueError
    integer_value = int(value)
    processed_value = integer_value * 2
    return processed_value
  except ValueError as e:
    print(f"Error: Invalid value provided. Cannot convert '{value}' to an integer. Encountered built-in exception: {e}")
    return None

valid_input = "123"
invalid_input = "abc"

result1 = process_value(valid_input)
if result1 is not None:
  print(f"Processed value of '{valid_input}': {result1}")

result2 = process_value(invalid_input)
if result2 is None:
  print(f"Processing of '{invalid_input}' failed.")