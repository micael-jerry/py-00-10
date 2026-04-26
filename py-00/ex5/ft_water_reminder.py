def ft_water_reminder():
    day: int = int(input("Days since last watering: "))
    status: str = "Water the plants!" if (day > 2) else "Plants are fine"

    print(status)
