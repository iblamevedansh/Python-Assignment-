def safe_getattr(obj, attribute_name, default=None):
    
  try:
    return getattr(obj, attribute_name)
  except AttributeError as e:
    if default is not None:
      print(f"Warning: Object of type '{type(obj).__name__}' has no attribute '{attribute_name}'. Returning default value.")
      return default
    else:
      print(f"Error: Object of type '{type(obj).__name__}' has no attribute '{attribute_name}'. Encountered built-in exception: {e}")
      return None

class MyClass:
  def __init__(self):
    self.data = 42

obj = MyClass()

value1 = safe_getattr(obj, "data")
print(f"Value of 'data': {value1}")

value2 = safe_getattr(obj, "missing_attribute", 0)
print(f"Value of 'missing_attribute' (with default): {value2}")

value3 = safe_getattr(obj, "another_missing_attribute")
print(f"Value of 'another_missing_attribute' (no default): {value3}")

method_value = safe_getattr(obj, "non_existent_method")
print(f"Value of 'non_existent_method': {method_value}")