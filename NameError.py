def get_variable(variable_name):

  try:
    value = eval(variable_name)
    return value
  except NameError as e:
    print(f"Error: Variable '{variable_name}' is not defined. Built-in exception: {e}")
    return None

defined_var = 10
undefined_var_name = "non_existent_variable"

value1 = get_variable("defined_var")
if value1 is not None:
  print(f"Value of defined_var: {value1}")

value2 = get_variable(undefined_var_name)
if value2 is None:
  print(f"Attempt to access '{undefined_var_name}' failed.")