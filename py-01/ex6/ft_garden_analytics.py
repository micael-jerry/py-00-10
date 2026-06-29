#!/usr/bin/env python3

class Plant:
    # TODO: affichage function
    __grow_call: int = 0
    __age_call: int = 0
    __show_call: int = 0

    def __init__(self, name: str, height: int, age: int):
        self.__name: str = name
        self.__height: float = float(height)
        self.__age: int = age
        self.__growth_per_day: float = round(self.__height / self.__age, 1)

        print(
            f"Plant created: {self.__name}: {self.__height}cm, {self.__age} days old")

    @staticmethod
    def isOlderThanYear(age: int) -> bool:
        return age > 365

    @classmethod
    def createPlantAnonymous(cls) -> Plant:
        return cls("Anonymous Plant", 0, 0)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def height(self) -> float:
        return self.__height

    @property
    def age(self) -> int:
        self.__age_call += 1
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
        self.__show_call += 1
        return f"{self.__name}: {self.__height}cm, {self.__age} days old"

    def grow(self) -> None:
        self.__height = round(self.__height + self.__growth_per_day, 1)
        self.__grow_call += 1

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


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.__color: str = color
        self.__is_blooming: bool = False

    def __str__(self) -> str:
        return f"""{super().__str__()}
 Color: {self.__color}
 {"Rose is blooming beautifully!" if self.__is_blooming else "Rose has not bloomed yet"}"""

    def bloom(self) -> None:
        if (self.__is_blooming):
            print(f"{self.__name}: Already blooming!")
            return
        print("[asking the rose to bloom]")
        self.__is_blooming = True

class Tree(Plant):
    # TODO: affichage function
    __produce_shade_call: int = 0

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.__trunk_diameter: float = float(trunk_diameter)

    def __str__(self) -> str:
        return f"""{super().__str__()}
 Trunk diameter: {round(self.__trunk_diameter, 1)}cm"""

    def produce_shade(self) -> None:
        self.__produce_shade_call += 1
        print("[asking the oak to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.height}cm long and {round(self.__trunk_diameter, 1)}cm wide.")

class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.__harvest_season: str = harvest_season
        self.__nutritional_value: int = 0

    def __str__(self) -> str:
        return f"""{super().__str__()}
 Harvest season: {self.__harvest_season}
 Nutritional value: {self.__nutritional_value}"""

    def grow(self) -> None:
        super().grow()
        self.__nutritional_value += 0.5

    def up_age(self) -> None:
        super().up_age()
        self.__nutritional_value += 0.5

class Seed(Flower):
    def __init__(self, name: str, height: int, age: int, color: str, seeds: int):
        super().__init__(name, height, age, color)
        self.__seeds = seeds

    def __str__(self) -> str:
        return f"""{super().__str__()}
 Color: {self.__color}
 Seeds: {self.__seeds if self.__is_blooming else "not bloomed yet"}
 {"Rose is blooming beautifully!" if self.__is_blooming else "Rose has not bloomed yet"}"""


# TODO: verify grow method
def main() -> None:
    print("=== Garden Statics ===")
    print("=== Check year old")
    print(f"Is 30 days more than a year? -> {Plant.isOlderThanYear(30)}")
    print(f"Is 400 days more than a year? -> {Plant.isOlderThanYear(400)}")

    print("=== Flower")
    rose: Flower = Flower("Rose", 15, 10, "Red")
    print(rose)
    rose.bloom()
    print(rose, "\n")

    print("=== Tree")
    oak: Tree = Tree("Oak", 200, 100, 5)
    print(oak)
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato: Vegetable = Vegetable("Tomato", 5, 10, "April")
    print(tomato)
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.up_age()

    print(tomato)

if __name__ == "__main__":
    main()
