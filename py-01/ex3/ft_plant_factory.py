#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.__name: str = name
        self.__height: float = float(height)
        self.__age: int = age
        self.__growth_per_day: float = round(self.__height / self.__age, 1)

        print(
            f"Plant created: {self.__name}: {self.__height}cm, {self.__age} days old")

    def __str__(self) -> str:
        return f"{self.__name}: {self.__height}cm, {self.__age} days old"

    def grow(self) -> None:
        self.__height = round(self.__height + self.__growth_per_day, 1)

    def age(self) -> None:
        self.__age += 1

    def growth_simulation(self, num_of_days: int) -> None:
        plant_cp: Plant = Plant(self.__name, self.__height, self.__age)

        print("=== Garden Plant Growth ===")

        for day in range(num_of_days):
            print(f"=== Day {day + 1} ===")
            plant_cp.grow()
            plant_cp.age()
            print(
                f"{plant_cp.__name}: {plant_cp.__height}cm, {plant_cp.__age} days old")

        print(
            f"Growth this week: {round(plant_cp.__height - self.__height)}cm")


def main() -> None:
    plant_list: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Tulip", 20, 25),
        Plant("Lily", 30, 35),
        Plant("Sunflower", 10, 5),
        Plant("Daisy", 15, 20)
    ]

    for plant in plant_list:
        print(plant)


if __name__ == "__main__":
    main()
