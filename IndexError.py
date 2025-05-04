def get_list_item(data_list, index):

  try:
    item = data_list[index]
    return item
  except IndexError as e:
    print(f"Error: Index out of bounds. Encountered built-in exception: {e}")
    return None

my_list = [10, 20, 30]

item1 = get_list_item(my_list, 1)
if item1 is not None:
  print(f"Item at index 1: {item1}")

item2 = get_list_item(my_list, 5)
if item2 is None:
  print("Attempted to access an index that does not exist.")

item3 = get_list_item(my_list, -1)
if item3 is not None:
  print(f"Item at index -1: {item3}")

item4 = get_list_item(my_list, -5)
if item4 is None:
  print("Attempted to access a negative index that is out of bounds.")