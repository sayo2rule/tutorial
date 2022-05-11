import random
random.seed(345)

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

# To produce a random floating number between the least possible number and an integer
# simply multiply by the integer
random_float_1_5 = random.random() * 5
print(random_float_1_5)

# Using this knowledge to build the love score app
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# Using it in throwing a die game
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print(f"Your dice values are {dice1} and {dice2}")



