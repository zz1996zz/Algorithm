
class Solution:
    def numIslands(self, grid) -> int:
        def dfs(i, j):
            # i, j가 범위에 벗어난 값이거나 육지(1)가 아니면 return 한다.
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '0'

            # grid[i][j]를 기준으로 동서남북 다 탐색하여 육지인지 확인한다.
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count

answer = Solution()
print(answer.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(answer.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

