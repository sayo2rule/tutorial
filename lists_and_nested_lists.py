states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina", "New Hampshire",  "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama",
                     "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
                     "Oregon", "Kansas", "West Virginia", "Nevada",  "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana",
                     "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(len(states_of_america))

# List offset starts from 0 instead of 1
print(states_of_america[2])

# Negative will start from the rare
print(states_of_america[-1])
print(states_of_america[-3])

# Change the content in any offset
print(states_of_america[1])
states_of_america[1] = "Pencilvania"
print(states_of_america[1])
states_of_america[1] = "Pennsylvania"
print(states_of_america[1])

# Add to the list
states_of_america.append("Angel land")
print(len(states_of_america))
print(states_of_america[50])
num_of_states = (len(states_of_america))

# Last person on the list
last_state_in_the_state = (num_of_states - 1)

print(states_of_america[last_state_in_the_state])

# # More on Data structure
# states_of_america.extend = (["Example1", "Example2"])
# states_of_america.insert(1, "Example3")
# states_of_america.remove([2, 3])
# states_of_america.pop()
# states_of_america.clear()
# states_of_america.index()
# states_of_america.count()
# states_of_america.sort()
# states_of_america.copy()
# print(states_of_america)

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectaries", "Apples",
               "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectaries", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)