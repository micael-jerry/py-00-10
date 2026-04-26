def ft_count_harvest_iterative():
  day: int = int(input("Days until harvest: "))

  if day < 1:
    return

  for i in range(1, day + 1):
    print(f"Day {i}")

  print("Harvest time!")