from collections import Counter

N = int(input())
cards = list(map(int, input().split()))
cards_counter = Counter(cards)

M = int(input())

targets = list(map(int, input().split()))


for target in targets:
    print(cards_counter[target], end=' ')