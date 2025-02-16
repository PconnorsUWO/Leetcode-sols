def getRow(rowIndex):
#     res = []
#     def get_num(cur_col, cur_row):
#         if cur_col == 0 or cur_col == cur_row:
#             return 1
#         return get_num(cur_col - 1, cur_row - 1) + get_num(cur_col, cur_row - 1)
#     for i in range(rowIndex + 1):
#         res.append(get_num(i, rowIndex))
#     return res
        N = rowIndex + 2
        res = [0]*N
        for i in range(N):
            res[i] = [1]*i
            for j in range(1,i-1):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res[-1]



# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
case1 = 3
print(getRow(case1))
# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 