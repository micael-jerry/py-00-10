def garden_operations(operation_number: int) -> None:
  match operation_number:
    case 0:
      int("abc")
    case 1:
      4 / 0
    case 2:
      open("test.txt")
    case 3:
      print("a" + 2)

def test_error_types() -> None:
  try:
    garden_operations(0)
  except ValueError as ve:
    print(ve)

  try:
    garden_operations(1)
  except ZeroDivisionError as zde:
    print(zde)

  try:
    garden_operations(2)
  except FileNotFoundError as fnfe:
    print(fnfe)
  
  try:
    garden_operations(3)
  except TypeError as te:
    print(te)

if __name__ == "__main__":
  test_error_types()