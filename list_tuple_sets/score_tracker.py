# Stores student scores in a list
scores = [78, 95, 88, 67, 100]


# Finds the highest score
print("Highest score:", max(scores))
# Finds the lowest score
print("Lowest score:", min(scores))

# Calculates the average score
print("Average Score:" , sum(scores) / len (scores))

# Sorts scores from highest to lowest
scores.sort(reverse=True)
print("Sorted scores (highest to lowest):", scores)

