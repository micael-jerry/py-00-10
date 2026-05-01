#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.__name = name
        self.__height = height
        self.__age = age

    def __str__(self) -> str:
        return f"{self.__name}: {self.__height}cm, {self.__age} days old"


def main() -> None:
    plant_list: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Tulip", 20, 25),
        Plant("Lily", 30, 35)
    ]

    for plant in plant_list:
        print(plant)


if __name__ == "__main__":
    main()
