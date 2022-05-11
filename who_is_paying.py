import random

# Don't change the code below
test_seed = int(input("Create a seed: "))
random.seed(test_seed)

# Split string method
names_as_CSV = input("Give me everybody's names, separated by a coma and a space. ")
names = names_as_CSV.split(",")

# Don't worry about lines 3/4. It's there to allow us to test your code.
# Write your code below this line

print(f'The names of everyone is as follows {names}')
# Let x rep the position of the last person on the list
x = len(names) - 1
random_choice = random.randint(0, x)
name_in_random_choice = names[random_choice]
print(f'The person that will pay the bill is {name_in_random_choice}')
