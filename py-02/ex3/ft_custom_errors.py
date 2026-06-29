class GardenError(Exception):
  def __init__(self, msg = "Garden Error default message"):
    super().__init__(msg)

class PlantError(GardenError):
  def __init__(self, msg="Plant Error default message"):
    super().__init__(msg)

class WaterError(GardenError):
  def __init__(self, msg="Water Error default message"):
    super().__init__(msg)

def test_custom_exception():
  try:
    raise PlantError("Plant Error")
  except PlantError as e:
    print(f"Caught PlantError: {e}")

  try:
    raise WaterError("Water Error")
  except WaterError as e:
    print(f"Caught WaterError: {e}")

if __name__ == "__main__":
  test_custom_exception()