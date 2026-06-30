import sys

def main() -> None:
  argv: list[str] = sys.argv

  print("=== Command Quest ===")
  print(f"Program name: {argv[0]}")

  if len(argv) == 1:
    print("No arguments provided!")
  else:
    print(f"Arguments received: {len(argv) - 1}")
    i = 1
    while i < len(argv):
      print(f"Argument {i}: {argv[i]}")
      i += 1
  print(f"Total arguments: {len(argv)}")

if __name__ == "__main__":
  main()
