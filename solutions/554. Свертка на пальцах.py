n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
B = [list(map(int, input().split())) for _ in range(k)]

n_rows = n - k + 1
n_cols = m - k + 1

C = [[0] * n_cols for _ in range(n_rows)]

for i in range(n_rows):
    for j in range(n_cols):
        s_val = 0
        for p in range(k):
            for q in range(k):
                s_val += A[i + p][j + q] * B[p][q]
        C[i][j] = s_val

for row in C:
    print(' '.join(map(str, row)))
