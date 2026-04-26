def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    display_quantity_with_unit: str

    if unit == "packets":
        display_quantity_with_unit = f"{quantity} packets available"
    elif unit == "grams":
        display_quantity_with_unit = f"{quantity} grams total"
    elif unit == "area":
        display_quantity_with_unit = f"covers {quantity} square meters"

    print(f"{seed_type.capitalize()} seeds: {display_quantity_with_unit}")
