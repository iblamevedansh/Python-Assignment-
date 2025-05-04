def get_value_from_dict(data_dict, key):

  try:
    value = data_dict[key]
    return value
  except KeyError as e:
    print(f"Error: Key '{key}' not found in the dictionary. Encountered built-in exception: {e}")
    return None

my_dictionary = {"name": "Alice", "age": 30, "city": "New York"}

name = get_value_from_dict(my_dictionary, "name")
if name is not None:
  print(f"Name: {name}")

country = get_value_from_dict(my_dictionary, "country")
if country is None:
  print("Could not retrieve country.")