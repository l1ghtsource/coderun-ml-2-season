def levenshtein_distance(s, t, k):
    m, n = len(s), len(t)

    if abs(m - n) > k:
        return k + 1

    previous_row = list(range(n + 1))
    current_row = [0] * (n + 1)

    for i in range(1, m + 1):
        current_row[0] = i
        min_value = i

        start = max(1, i - k)
        end = min(n, i + k)

        for j in range(start, end + 1):
            if s[i - 1] == t[j - 1]:
                current_row[j] = previous_row[j - 1]
            else:
                current_row[j] = 1 + min(
                    previous_row[j],
                    current_row[j - 1],
                    previous_row[j - 1]
                )
            min_value = min(min_value, current_row[j])

        if min_value > k:
            return k + 1

        previous_row, current_row = current_row, previous_row

    return previous_row[n]


t = int(input().strip())
results = []

for _ in range(t):
    k = int(input().strip())
    s = input().strip()
    t = input().strip()

    if levenshtein_distance(s, t, k) <= k:
        results.append('Yes')
    else:
        results.append('No')

for result in results:
    print(result)
