#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.__name: str = name
        self.__height: float = float(height)
        self.__age: int = age
        self.__growth_per_day: float = round(self.__height / self.__age, 1)

        print(
            f"Plant created: {self.__name}: {self.__height}cm, {self.__age} days old")

    @property
    def name(self) -> str:
        return self.__name

    @property
    def height(self) -> float:
        return self.__height

    @property
    def age(self) -> int:
        return self.__age

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @height.setter
    def height(self, height: int) -> None:
        if (height < 0):
            print(f"{self.__name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self.__height = float(height)
        print(f"Height updated: {height}cm")

    @age.setter
    def age(self, age: int) -> None:
        if (age < 0):
            print(f"{self.__name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self.__age = age
        print(f"Age updated: {age} days")

    def __str__(self) -> str:
        return f"{self.__name}: {self.__height}cm, {self.__age} days old"

    def grow(self) -> None:
        self.__height = round(self.__height + self.__growth_per_day, 1)

    def up_age(self) -> None:
        self.__age += 1

    def growth_simulation(self, num_of_days: int) -> None:
        plant_cp: Plant = Plant(self.__name, self.__height, self.__age)

        print("=== Garden Plant Growth ===")

        for day in range(num_of_days):
            print(f"=== Day {day + 1} ===")
            plant_cp.grow()
            plant_cp.up_age()
            print(
                f"{plant_cp.__name}: {plant_cp.__height}cm, {plant_cp.__age} days old")

        print(
            f"Growth this week: {round(plant_cp.__height - self.__height)}cm")


def main() -> None:
    print("=== Garden Security System ===")

    plant: Plant = Plant("Rose", 15, 10)
    print()

    plant.height = 25
    plant.age = 30
    print()

    plant.height = -10
    plant.age = -20
    print()

    print(
        f"Current State: {plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    main()
