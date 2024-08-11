def solve(n, s, arrivals):
    if s >= n:
        return 'INF'

    arrivals.sort()

    min_diff = float('inf')
    for i in range(n - s):
        diff = arrivals[i + s] - arrivals[i]
        min_diff = min(min_diff, diff)

    return min_diff if min_diff > 0 else 'Impossible'


n, s = map(int, input().split())
arrivals = [int(input()) for _ in range(n)]

result = solve(n, s, arrivals)
print(result)
