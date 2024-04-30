K, N = map(int, input().split())
lan_cables = [int(input()) for _ in range(K)]

start, end = 1, max(lan_cables)

while start <= end:
    mid = (start + end) // 2
    lines = sum([cable // mid for cable in lan_cables])
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)