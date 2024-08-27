import math
import heapq


def euclidean_distance(features1, features2):
    return math.sqrt(sum((f1 - f2) ** 2 for f1, f2 in zip(features1, features2)))


def find_similar_items(items, query, top_k=5):
    target_item = items[query['index']]
    available_items = []

    for i, item in enumerate(items):
        if item['available'] and item['price'] <= query['money']:
            dist = euclidean_distance(target_item['features'], item['features'])
            available_items.append((dist, i))

    top_items = heapq.nsmallest(top_k, available_items)
    return [i for _, i in top_items]


n, q = map(int, input().split())

items = []
for _ in range(n):
    parts = list(map(int, input().split()))
    items.append({
        'available': parts[0],
        'price': parts[1],
        'features': parts[2:]
    })

queries = []
for _ in range(q):
    parts = list(map(int, input().split()))
    queries.append({
        'index': parts[0],
        'money': parts[1]
    })

results = []

for query in queries:
    target_item = items[query['index']]

    if target_item['available'] and target_item['price'] <= query['money']:
        results.append((1, [query['index']]))
    else:
        similar_items = find_similar_items(items, query)
        results.append((5, similar_items))

for count, indices in results:
    print(count)
    print(' '.join(map(str, indices)))
