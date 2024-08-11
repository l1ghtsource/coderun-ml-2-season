import sys


def count_cats(grid):
    m = len(grid)
    n = len(grid[0])
    cat_count = 0
    result = [[0 for _ in range(n)] for _ in range(m)]

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or result[i][j] != 0:
            return
        result[i][j] = cat_count
        for di, dj in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            dfs(i + di, j + dj)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and result[i][j] == 0:
                cat_count += 1
                dfs(i, j)

    return cat_count, result


input = sys.stdin.read
data = input().strip().split('\n')
grid = [list(map(int, row.split())) for row in data]
cat_count, result = count_cats(grid)

print(cat_count)
for row in result:
    print(' '.join(map(str, row)))
