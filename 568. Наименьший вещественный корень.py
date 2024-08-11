import numpy as np
from scipy.linalg import eigvals


def solve(n, A, B):
    I = np.eye(n)
    O = np.zeros((n, n))
    M = np.vstack((np.hstack((O, I)), np.hstack((-B, -A))))

    real_eigenvalues = [ev.real for ev in eigvals(M) if np.isreal(ev)]
    smallest_real_root = min(real_eigenvalues)

    return np.round(smallest_real_root, 4)


n = int(input())
A = []
for _ in range(n):
    A.append(list(map(float, input().split())))
A = np.array(A)

B = []
for _ in range(n):
    B.append(list(map(float, input().split())))
B = np.array(B)

print(solve(n, A, B))
