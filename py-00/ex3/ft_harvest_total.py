def ft_harvest_total():
    total: int = 0

    for i in [1, 2, 3]:
        harvest: int = int(input(f"Day {i} harvest: "))
        total += harvest

    print(f"Total harvest: {total}")
