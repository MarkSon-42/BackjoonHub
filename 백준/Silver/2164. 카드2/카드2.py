from collections import deque

N = int(input())
cards = deque(range(1, N+1))

while len(cards) > 1:
    cards.popleft()  # 제일 위에 있는 카드를 버린다
    cards.rotate(-1)  # 제일 위에 있는 카드를 제일 아래로 옮긴다

print(cards[0])