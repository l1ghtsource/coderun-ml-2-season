import numpy as np

n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
C = [list(map(int, input().split())) for _ in range(n - k + 1)]

coeffs = []
for i in range(n - k + 1):
    for j in range(m - k + 1):
        for p in range(k):
            for q in range(k):
                coeffs.append(A[i + p][j + q])

vec = []
for row in C:
    vec.extend(row)

coeffs = np.array(coeffs).reshape(-1, k * k)
vec = np.array(vec)

B_flatten, _, _, _ = np.linalg.lstsq(coeffs, vec, rcond=None)
B = B_flatten.reshape(k, k).round().astype(int)

for row in B:
    print(' '.join(map(str, row)))
