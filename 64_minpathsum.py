from typing import List
def minPathSum(grid: List[List[int]]) -> int:
    # num_row, num_col = len(grid) - 1, len(grid[0]) - 1
    # directions = [(1, 0), (0, 1)]
    # res = float("inf")
    # def dfs(cur_cost, position):
    #     nonlocal res
    #     row, col = position
    #     if row > num_row or col > num_col or cur_cost >= res:
    #         return
    #     if row == num_row and col == num_col:
    #         res = min(cur_cost + grid[row][col],res)
    #         return

    #     for dr, dc in directions:
    #         new_position = (row + dr, col + dc)
    #         dfs(cur_cost + grid[row][col], new_position)
        
    # dfs(0, (0, 0))
    # return res
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j != n - 1:
                dp[i][j] = grid[i][j] + dp[i][j + 1]
            elif j == n - 1 and i != m - 1:
                dp[i][j] = grid[i][j] + dp[i + 1][j]
            elif j != n - 1 and i != m - 1:
                dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
            else:
                dp[i][j] = grid[i][j]
    return dp[0][0]
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:
case1 = [[1,3,1],[1,5,1],[4,2,1]]
case2 = [[0,7,7,8,1,2,4,3,0,0,5,9,8,3,6,5,1,0],[2,1,1,0,8,1,3,3,9,9,5,8,7,5,7,5,5,8],[9,2,3,1,2,8,1,2,3,7,9,7,9,3,0,0,3,8],[3,9,3,4,8,1,2,6,8,9,3,4,9,4,8,3,6,2],[3,7,4,7,6,5,6,5,8,6,7,3,6,2,2,9,9,3],[2,3,1,1,5,4,7,4,0,7,7,6,9,1,5,5,0,3],[0,8,8,8,4,7,1,0,2,6,1,1,1,6,4,2,7,9],[8,6,6,8,3,3,5,4,6,2,9,8,6,9,6,6,9,2],[6,2,2,8,0,6,1,1,4,5,3,1,7,3,9,3,2,2],[8,9,8,5,3,7,5,9,8,2,8,7,4,4,1,9,2,2],[7,3,3,1,0,9,4,7,2,3,2,6,7,1,7,7,8,1],[4,3,2,2,7,0,1,4,4,4,3,8,6,2,1,2,5,4],[1,9,3,5,4,6,4,3,7,1,0,7,2,4,0,7,8,0],[7,1,4,2,5,9,0,4,1,4,6,6,8,9,7,1,4,3],[9,8,6,8,2,6,5,6,2,8,3,2,8,1,5,4,5,2],[3,7,8,6,3,4,2,3,5,1,7,2,4,6,0,2,5,4],[8,2,1,2,2,6,6,0,7,3,6,4,5,9,4,4,5,7]]

print(minPathSum(case2))
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12