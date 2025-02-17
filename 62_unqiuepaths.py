def uniquePaths(m,n):
    # paths = 0  
    # directions = [(1, 0), (0, 1)]
    
    # def dfs(row, col):
    #     nonlocal paths
    #     if row == m - 1 and col == n - 1:
    #         paths += 1
    #         return
    #     if row >= m or col >= n:
    #         return
    #     for dr, dc in directions:
    #         dfs(row + dr, col + dc)
    
    # dfs(0, 0)
    # return paths
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp

# Input: m = 3, n = 7
# Output: 28
# Example 2:
case1 = [3,7]
print(uniquePaths(*case1))
case2 = [1,2]
print(uniquePaths(*case2))

# Input: m = 3, n = 2
# Output: 3