import numpy as np
from sklearn.cluster import MiniBatchKMeans
from scipy.optimize import minimize

filename = 'data.txt'

with open(filename, 'r') as file:
    first_line = file.readline().strip().split()
    k = int(first_line[0])
    n = int(first_line[1])
    c_cost = int(first_line[2])
    C = int(first_line[3])

    homes = []
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            homes.append((int(parts[0]), int(parts[1])))

homes = np.array(homes)

kmeans = MiniBatchKMeans(n_clusters=k, batch_size=1000, random_state=42)
kmeans.fit(homes)
quarters = kmeans.cluster_centers_


def calculate_profit():
    profit = C

    for quarter_idx in range(k):
        closest_point = quarters[quarter_idx]

        closest_homes_indices = kmeans.labels_ == quarter_idx
        total_distance = 0.0
        count = np.sum(closest_homes_indices)

        if count > 0:
            for home_idx in np.where(closest_homes_indices)[0]:
                distance = np.linalg.norm(homes[home_idx] - closest_point)
                total_distance += (distance ** (1 / 4)) + 1

            profit -= c_cost * total_distance / count

    return -profit


x0 = np.zeros(k, dtype=int)

result = minimize(calculate_profit, x0, method='nelder-mead', options={'disp': True})

print(-result.fun)
print(result.x)
