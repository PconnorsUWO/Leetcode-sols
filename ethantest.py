def min_moves(arr) -> int: 
    cost = 0
    N = len(arr)
    minimum = arr[0]
    for i in range(0,N):
        if (arr[i] - minimum) % 2 == 0 or (arr[i] - minimum) == 0:
            continue
        else:
            cost += 1
    return cost



case1 = [1,2,3]
print(min_moves(case1)) 
case2 = [2,2,2,3,3]
case3 = [1,1000000000]
print(min_moves(case2))
print(min_moves(case3))