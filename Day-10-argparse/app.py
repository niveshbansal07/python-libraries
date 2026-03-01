import argparse



parser = argparse.ArgumentParser(description="Simple greeting CLI")

parser.add_argument("--name", type=str, help="Enter your name")

args = parser.parse_args()

print(f"Hello {args.name}")

