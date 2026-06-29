def input_temperature(temp_str: str) -> int:
  MIN_TEMP = 0
  MAX_TEMP = 40

  print(f"Input data is '{temp_str}'")

  try:
    temp:int = int(temp_str)
    if temp > MAX_TEMP:
      raise ValueError(f"{temp} is too hot for plants (max {MAX_TEMP}°C)")
    elif temp < MIN_TEMP:
      raise ValueError(f"{temp}  is too cold for plants (min {MIN_TEMP}°C)")
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
    test_temperature(100)
    test_temperature(-50)
