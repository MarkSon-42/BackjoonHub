n, q = map(int, input().split(" "))

balloon_state = [None for x in range(n)]

for i in range(q):
    L, I = map(int, input().split(" "))

    for index in range(L - 1, n, I):
        balloon_state[index] = "balloon"

blank_slot = balloon_state.count(None)

print(blank_slot)
