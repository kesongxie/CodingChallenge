import math
# A child is running a staircase with n steps, and can hop either 1 step, 2 steps,
# or 3 steps at a time. Implement a method so
# to count how many possible ways the child can run up the stairs


#tags: recursion, dynamic programming
#stregies: using dynamic programming to memory the previously caculated ways
def countStairWay(n, map):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    elif n in map:
        return map[n]
    else:
        map[n] = countStairWay(n-1, map) + countStairWay(n-2, map) + countStairWay(n-3, map)
        return map[n]

#TEST countStairWay
#map = {0: 0}
#print(countStairWay(100, map))

# -------------------------------------------------------------------------------------------------- #


# imagine a robot sitting on the upper left corner of an X by Y grid.
# The robot can only move in two directions: right and down
# How many possible paths are there for the robot to go from (0, 0) to (X, Y)

# Approach 1
# tags: recursion, dynamic programming
# strategies: using dynamic programming to memory the previously caculated ways

def gridMovingCount(x, y, cache):
    if x == 0 or y == 0:
        return 1
    elif (x,y) in cache:
        return cache[(x,y)]
    else:
        cache[(x,y)] = gridMovingCount(x-1, y, cache) + gridMovingCount(x, y-1, cache)
        return cache[(x,y)]


# Approach 2
# tags: counting
# strategies: using binomial counting, pick x out x+y step for walking right

def gridMovingCountByBinomial(x, y):
    # use explict // for true division, otherwise, a estimation will be given for classic division /
    return math.factorial(x + y) // (math.factorial(x) * math.factorial(y))


# cache = {"":0}
# print(gridMovingCount(50, 50, cache))
# print(gridMovingCountByBinomial(50, 50))

# -------------------------------------------------------------------------------------------------- #

unAvailablePoint = [(1, 2), (3, 0), (0, 3), (2, 3), (0, 1)]

def steppable(point):
    return point not in unAvailablePoint

def travel(x, y, path, visited):
    if x >= 0 and y >= 0 and steppable((x, y)):
        if (x, y) in visited:
            return visited[(x, y)]
        success = False
        if (x, y) == (0, 0) or travel(x-1, y, path, visited) or travel(x, y-1, path, visited):
            path.append([(x, y)]) #use append instead of +, we want to modify the original reference of the list
            #path += [(x,y)]  also works, this will modify the path variable
            success = True
        visited[(x, y)] = success
        return success
    return False

path = []
visited = {}
travel(3, 3, path, visited)
print(path)
# what I Learnt: the path is not defined until there is one recursive call that leads to the
# origin (0, 0). Since the question is asking for a path, stop recursive call once you find the origin.
# As the function back track from the recursive call, it will lead to a path from the given (x, y) to the origin (0, 0)
# if existed.

