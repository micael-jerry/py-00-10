import sys as s

def str_to_int(s: str) -> int:
  try:
    return int(s)
  except Exception as e:
    print(f"Caught str_to_int: {s} is not a valid integer")

def str_lst_to_int_lst(str_list: list[str]) -> list[int]:
  res: list[int] = []
  try:
    i: int = 0
    while i < len(str_list):
      res.append(str_to_int(str_list[i]))
      i += 1
  except Exception as e:
    print(e)

def main():
  print("=== Player Score Analytics ===")
  argv: list[str] = s.argv

  if len(argv) == 1:
    print("No arguments")
    return

  parsed: list[int] = str_lst_to_int_lst(argv[1:])

  print(f"Scores processed: {parsed}")
  print(f"Total players: {len(parsed)}")
  print(f"Total score: {sum(parsed)}")
  print(f"Score average: {sum(parsed) / len(parsed)}")
  print(f"High score: {max(parsed)}")
  print(f"Low score: {min(parsed)}")
  print(f"Score range: {max(parsed) - min(parsed)}")

if __name__ == "__main__":
  main()
