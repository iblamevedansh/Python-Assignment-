def get_attribute_safely(obj, attribute_name):

  try:
    value = getattr(obj, attribute_name)
    return value
  except AttributeError as e:
    print(f"Error: Object of type '{type(obj).__name__}' has no attribute '{attribute_name}'. Encountered built-in exception: {e}")
    return None

class MyClass:
  def __init__(self):
    self.my_property = 10

obj1 = MyClass()
obj2 = []  

value1 = get_attribute_safely(obj1, "my_property")
if value1 is not None:
  print(f"Attribute 'my_property' of obj1: {value1}")

value2 = get_attribute_safely(obj2, "my_property")
if value2 is not None:
  print(f"Attribute 'my_property' of obj2: {value2}")

value3 = get_attribute_safely(obj1, "non_existent_method")