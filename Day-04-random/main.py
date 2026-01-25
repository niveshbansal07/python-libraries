import random

print("Random Number:", random.randint(1, 10))

names = ["Rahul", "Aman", "Neha", "Pooja"]
print("Lucky Winner:", random.choice(names))

cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print("Shuffled Cards:", cards)
