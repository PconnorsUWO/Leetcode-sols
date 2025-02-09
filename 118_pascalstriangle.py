# def generate(numRows):
#     res = [[]]
#     cur_row = 0
#     while len(res) <= numRows:
#         newRow = []
#         for i in range(cur_row+1):
#             if i == 0 or i == cur_row:
#                 newRow.append(1)
#             else:
#                 newRow.append(res[cur_row][i-1] + res[cur_row][i])
#         cur_row += 1
#         res.append(newRow)
#     return res[1:]

def generate(numRows):
    N = numRows + 1
    res = [0]*N
    res[0] = [1]
    for i in range(1,N):
        res[i] = [1]*i
        for j in range(1,i-1):
            res[i][j] = res[i-1][j-1] + res[i-1][j]
    return res[1:] 


# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
case1 = 50
print(generate(case1))
# Input: numRows = 1
# Output: [[1]]