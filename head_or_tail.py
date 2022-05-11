# Don't change the code below
import random
test_seed = int(input("Create a seed: "))
random.seed(test_seed)

# Write your code below this line

random_side = random.randint(0, 1)
if random_side == 1: 
    print("Heads")
else:
    print("Tails")