n, t = map(int, input().split())
times = list(map(int, input().split()))

times.sort()

count = 0
total_time = 0

for time in times:
    if total_time + time > t:
        break
    total_time += time
    count += 1

print(count)
