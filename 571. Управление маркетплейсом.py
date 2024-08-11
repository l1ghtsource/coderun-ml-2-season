import numpy as np
from collections import defaultdict

m, s = map(int, input().split())
n = int(input())

history = []
for _ in range(n):
    data = list(map(int, input().split()))
    w, d, h = data[:3]
    requests = data[3:]
    history.append((w, d, h, requests))

q = int(input())
queries = []
for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

data_hour = defaultdict(lambda: [])

for week, day, hour, requests in history:
    data_hour[(day, hour)].append(requests)


def predict(day, hour):
    if (day, hour) in data_hour and len(data_hour[(day, hour)]) > 0:
        return np.mean(data_hour[(day, hour)], axis=0)
    else:
        return np.zeros(m)


sliced_requests_sum = np.zeros(m)
prediction_count = 0

for query in queries:
    if query[0] == 1:
        w, d, h = query[1:4]
        requests = query[4:]
        data_hour[(d, h)].append(requests)
    elif query[0] == 2:
        w, d, h = query[1:4]
        predicted_requests = predict(d, h)
        remaining_requests = predicted_requests.copy()
        while s > 0 and np.sum(remaining_requests) > 0:
            for j in range(m):
                if remaining_requests[j] > 0 and s > 0:
                    remaining_requests[j] -= 1
                    s -= 1
        sliced_requests_sum += np.maximum(remaining_requests, 0)
        prediction_count += 1

if prediction_count > 0:
    average_sliced_requests = sliced_requests_sum / prediction_count
else:
    average_sliced_requests = np.zeros(m)

print(' '.join(map(str, average_sliced_requests)))
