import numpy as np


def random_point_in_cube():
    return np.random.rand(3)


def min_distance_to_vertex(point):
    vertices = np.array(
        [
            [0, 0, 0], [0, 0, 1],
            [0, 1, 0], [0, 1, 1],
            [1, 0, 0], [1, 0, 1],
            [1, 1, 0], [1, 1, 1]
        ]
    )
    distances = np.linalg.norm(vertices - point, axis=1)
    return np.min(distances)


num_points = 10 ** 10
threshold_distance = 3 / 4
count = 0

for _ in range(num_points):
    point = random_point_in_cube()
    if min_distance_to_vertex(point) > threshold_distance:
        count += 1

proba = count / num_points
print(proba)
