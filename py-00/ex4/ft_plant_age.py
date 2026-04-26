def ft_plant_age():
    plant_age: int = int(input("Enter plant age in days: "))
    status: str = "Plant is ready to harvest!" if (
        plant_age > 60) else "Plant is not ready to harvest!"

    print(status)
