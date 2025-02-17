def uniquePaths2(obstacleGrid):
    m,n = len(obstacleGrid),len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if (i == 0 or j == 0) and obstacleGrid[i][j] != 1:
                dp[i][j] = 1
            elif obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp

case1 = [[1,0]]
print(uniquePaths2(case1))