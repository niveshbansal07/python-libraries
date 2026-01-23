import sys

print("File Name:", sys.argv[0])

for arg in sys.argv[1:]:
    print("Argument:", arg)
