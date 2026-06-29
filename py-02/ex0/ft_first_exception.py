def input_temperature(temp_str: str) -> int:
  print(f"Input data is '{temp_str}'")

  try:
    return int(temp_str)
  except Exception as e:
    print(f"Caught input_temperature error : {e}")

def test_temperature(temp_str: str) -> None:
  try:
    temp: int = input_temperature(temp_str)
    print(f"Temperature is now {temp}°C")
  except Exception as e:
    print(e)

if __name__ == "__main__":
    test_temperature(25)
    test_temperature("abc")
