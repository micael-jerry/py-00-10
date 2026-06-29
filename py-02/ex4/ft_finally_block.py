class GardenError(Exception):
  def __init__(self, msg = "Garden Error default message"):
    super().__init__(msg)

class PlantError(GardenError):
  def __init__(self, msg="Plant Error default message"):
    super().__init__(msg)

class WaterError(GardenError):
  def __init__(self, msg="Water Error default message"):
    super().__init__(msg)

def water_plant(plant_name: str) -> None:
  if (plant_name.capitalize() == plant_name):
    print(f"Watering {plant_name} : [OK]")
    return
  raise PlantError(f"Invalid plant name to water: '{plant_name}'")

def test_finally_block():
  try:
    print("Opening watering system")
    water_plant("Tomato")
    water_plant("Lettuce")
    water_plant("Carrots")
  except Exception as e:
    print(e)
  finally:
    print("Closing watering system")

  try:
    print("Opening watering system")
    water_plant("Tomato")
    water_plant("lettuce")
  except PlantError as e:
    print(e)
  finally:
    print("Closing watering system")

if __name__ == "__main__":
  test_finally_block()