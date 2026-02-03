from pathlib import Path

path = Path("data/file.txt")

# print(path.exists())

folder = Path("reports")
folder.mkdir(exist_ok=True)

path.write_text("Everyone returns in avengers doomsday")
print(path.read_text())
