def print_days(day: int):
    if day < 1:
        return

    if day == 1:
        print("Day 1")
    else:
        print_days(day - 1)
        print(f"Day {day}")

def ft_count_harvest_recursive():
    day: int = int(input("Days until harvest: "))

    print_days(day)
    print("Harvest time!")
