#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.__name = name
        self.__height = height
        self.__age = age

    def __str__(self) -> str:
        return f"Plant: {self.__name}\nHeight: {self.__height}cm\nAge: {self.__age} days"


def main() -> None:
    plant = Plant("Rose", 25, 30)

    print("=== Welcome to My Garden ===")
    print(plant)
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
