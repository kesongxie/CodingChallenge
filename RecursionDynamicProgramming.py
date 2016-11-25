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

# path = []
# visited = {}
# travel(3, 3, path, visited)
# print(path)
# what I Learnt: the path is not defined until there is one recursive call that leads to the
# origin (0, 0). Since the question is asking for a path, stop recursive call once you find the origin.
# As the function back track from the recursive call, it will lead to a path from the given (x, y) to the origin (0, 0)
# if existed.


# find the magic index in a sorted distinct integer array such that A[i] = i, for example [-3, 0, 2, 3, 7, 9], the magic
# is 2, because A[2] = 2

def getMagicIndex(start, end, a):
    if start > end or start < 0 or end >= len(a):
        return -1
    mid = math.floor((start + end)/2)
    midValue = a[mid]
    if mid == midValue:
        return mid
    elif midValue > mid:
        return getMagicIndex(start, mid - 1, a)
    else:
        return getMagicIndex(mid + 1, end, a)

# A = [-3, 1, 4, 5, 7, 9]
# print(getMagicIndex(0, len(A) - 1, A))

# FOLLOW UP: what if the array A is not distinct
def getMagicIndexUndistinct(start, end, a):
    if start > end or start < 0 or end >= len(a):
        return -1
    mid = math.floor((start + end)/2)
    midvalue = a[mid]

    # search left
    endIndex = min(midvalue, mid - 1)
    leftFound = getMagicIndex(start, endIndex, a)
    if leftFound >= 0:
        return leftFound

    # search right
    startIndex = max(midvalue, mid + 1)
    rightFound = getMagicIndex(startIndex, end, a)
    return rightFound

# A = [-3, 0, 4, 6, 6, 6, 6, 9]
# print(getMagicIndexUndistinct(0, len(A) - 1, A))
# what I learnt: since the sorted list is not distinct, we can't just compare
# the mid index and the mid value to conclude which side to go.
# We have to search both left and right in order to not to miss the magic number if it does exist
# However, the left list and right list can be narrowed down if we know some information about the mid Value
# we have to take good advantage of the fact the list is sorted.
# It's always nice to


# -------------------------------------------------------------------------------------------------- #


def generateSubset(a,subset):
    if len(a) == 0:
        subset.append([])
    else:
        first = a[0]
        generateSubset(a[1: len(a)], subset)
        newSubSet = []
        for ele in subset:
            newEle = ele + [first]
            newSubSet.append(newEle)
        subset += newSubSet
mySet = [3, 5, 1]
subset = []
generateSubset(mySet, subset)
#print(subset)

# what I learnt: we can first get the subset of all the elements(sub array) without the first element
# for example -> for the original set [3, 5], get the subset of [5] , which is [ [], [5] ], then when we
# next we add 3, for each element in [ [], [5] ], we append 3 to the element , which is [ [3], [5, 3] ]. then we will
# just combine this two set together [ [], [5]] (this can be also viewed as a set without element 3)
# with [ [3], [5, 3] ] (this can be also viewed as a set with element 3), then we will have the final result.
# pay attention to the multiple dimension when doing appending


# -------------------------------------------------------------------------------------------------- #
def generatePermutation(string):
    stringLength = len(string)
    if stringLength == 0:
        return []
    elif stringLength == 1:
        return [string[0]]
    else:
        result = []
        firstChar = string[0]
        permutations = generatePermutation(string[1: stringLength])
        for permutate in permutations:
            for i in range(0, len(permutate) + 1):
                temp = permutate[:i] + firstChar + permutate[i:]
                result.append(temp)
        return result

string = "hol"
#print(len(generatePermutation(string)))

# what I learnt: break into sub problem. for "hol", generate the permutation for ol first, which is
# [ol, lo], then for each element in that sub-permutation, insert to any possible position of the element to complete
# the permutation of the original ol -> [hol, ohl, loh], and lo -> [hlo, lho, loh] with a nested loops


def getParen(n):
    if n == 0:
        return []
    elif n == 1:
        return ["[]"]
    else:
        result = []
        paren = "[]"
        for par in getParen(n - 1):
            for i in range(0, len(par)):
                temp = par[:i] + paren + par[i:]
                result.append(temp)
        return set(result)

print(getParen(3))