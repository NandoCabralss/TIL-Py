# Data Structures

# Lists 

heroes = ["Hulk", "Thor", "Iron Man", "Black Spider", "Loke", "Ant Man"]

how_many_thors = heroes.count("Hulk")
print(how_many_thors)

# Should print 1

thor_is_there = "Thor" in heroes
print(thor_is_there)

# Should print true

heroes.reverse()
print(heroes)

# Should print the reverse array starting with Ant Man

heroes.append("Spider Man")
print(heroes)

# Should print the same array with Spider Man in the end

heroes.sort()
print(heroes)

# Should print the array sorted

heroes.pop()
print(heroes)

# Should print the array without Thor
