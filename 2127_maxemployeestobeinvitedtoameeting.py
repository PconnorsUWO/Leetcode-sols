from typing import List
# we have n people
# given a circular table
# and a list favorite, where favorite[i] is a list of favorite people of person i
# return the maximum people that can sit at a table
# such that each person can sit next to their favorite person


def maximumInvitations(favorite: List[int]) -> int:
    if len(favorite) == 2:
        return 2
    dir_graph = {key: val for key, val in enumerate(favorite)}
    max_people = 0
    for i in dir_graph:
        j = i
        visited = {}
        step = 0
        transpositions = []
        while j not in visited:
            visited[j] = step
            step += 1
            j = dir_graph[j]
            if j not in dir_graph:
                break 
        if j in visited:
            cycle_length = step - visited[j]
            if cycle_length == 2:
                transpositions.append(cycle_length)
            max_people = max(max_people, cycle_length)
    if max_people == 2:
        return len(transpositions)*2 + 1
    return max_people

 

# Input: favorite = [2,2,1,2]
# Output: 3

# Input: favorite = [3,0,1,4,1]
# Output: 4

# Input: favorite = [1,2,0]
# Output: 3
case1 = [2,2,1,2]
case2 = [3,0,1,4,1]
case3 = [1,2,0]
print(maximumInvitations(case1))
