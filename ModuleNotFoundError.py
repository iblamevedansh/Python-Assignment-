def import_module_safely(module_name):
    
  try:
    module = __import__(module_name)
    return module
  except ModuleNotFoundError as e:
    print(f"Error: Module '{module_name}' not found. Please ensure it is installed. Encountered built-in exception: {e}")
    return None

math_module = import_module_safely("math")
if math_module:
  print(f"Successfully imported the '{math_module.__name__}' module.")
  print(math_module.sqrt(16))

non_existent_module = import_module_safely("non_existent_module_123")
if not non_existent_module:
  print("Failed to import the non-existent module.")