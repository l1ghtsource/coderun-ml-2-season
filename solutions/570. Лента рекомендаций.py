p, n, k = map(int, input().split())

themes = [input() for _ in range(p)]
ids = [int(i) for i in input().split()]

theme_count = {theme: 0 for theme in themes}
selected_count = 0
selected_videos = []

for i in range(p):
    theme, video_id = themes[i], ids[i]
    if theme_count[theme] < k:
        selected_videos.append(f'{theme} #{video_id}')
        theme_count[theme] += 1
        selected_count += 1
    if selected_count == n:
        break

for video in selected_videos:
    print(video)