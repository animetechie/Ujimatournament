import random

# Initialize the scores, pairings, and total points
scores = {}
pairings = {}
total_points = {}

# Set the flag variable to True
game_on = True

# Get the number of people
num_people = int(input("Enter the number of people who are battling: "))

# Get the names of the people
names = []
for i in range(num_people):
  name = input(f"Enter the name of person {i+1}: ")
  names.append(name)

# Main game loop
while game_on:
  # Sort the scores from highest to lowest
  sorted_scores = sorted(total_points.items(), key=lambda x: x[1], reverse=True)

  # Print the current scores
  print("Current scores:")
  for name, score in sorted_scores:
    print(f"{name}: {score} points")

  # Shuffle the names
  random.shuffle(names)

  # Pair the names
  for i in range(0, len(names), 2):
    name1 = names[i]
    name2 = names[i+1]
    print(f"{name1} will fight {name2}")
    pairings[name1] = name2
    pairings[name2] = name1

  # Get the number of wins for each person
  for name in names:
    wins = int(input(f"Enter the number of wins for {name}: "))
    scores[name] = wins

  # Assign points based on the number of wins
  for name in names:
    wins = scores[name]
    if wins == 2:
      scores[name] = 75
    elif wins == 1:
      scores[name] = 25

    # Update the total points for the person
    if name in total_points:
      total_points[name] += scores[name]
    else:
      total_points[name] = scores[name]

  # Ask if there will be another set of rounds
  another_round = input("Do you want to play another round (y/n)? ")
  if another_round == "n":
    game_on = False

# Sort the total points from highest to lowest
sorted_total_points = sorted(total_points.items(), key=lambda x: x[1], reverse=True)

# Print the top eight scorers will be gym leaders
print("Your top eight scorers will be gym leaders:")
for i in range(8):
  name, points = sorted_total_points[i]
  print(f"{name}: {points} points")

# Print all the final scores from highest to lowest
print("Final scores:")
for name, points in sorted_total_points:
  print(f"{name}: {points} points")
