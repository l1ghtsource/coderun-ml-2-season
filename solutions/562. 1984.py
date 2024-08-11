def literally_1984(stop_words, message):
    for word in stop_words:
        if word in message:
            return 'DELETE'
    return 'KEEP'


n, m = map(int, input().split())
stop_words = [input() for _ in range(n)]
messages = [input() for _ in range(m)]

for message in messages:
    result = literally_1984(stop_words, message)
    print(result)
