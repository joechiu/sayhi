import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: sayhi <name>")
        sys.exit(1)

    name = sys.argv[1]
    print(f"Hello, {name}!")

