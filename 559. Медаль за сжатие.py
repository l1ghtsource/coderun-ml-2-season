import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import sys


def read_input():
    input = sys.stdin.read().strip().split('\n')
    n, m, p = map(float, input[0].strip().split())
    n, m = int(n), int(m)
    data = []
    for line in input[1:]:
        data.append(list(map(float, line.strip().split())))
    data = np.array(data)
    return n, m, p, data


n, m, p, data = read_input()
features = data[:, :-1]

scaler = StandardScaler()
pca = PCA(n_components=int(2 * m / 3))

features_reduced = pca.fit_transform(scaler.fit_transform(features))

print(int(features_reduced.shape[1]))
for feature_set in features_reduced:
    print(*feature_set)
