def solution(bandage, health, attacks):
    answer = health
    idx = 0
    lastIdx = len(attacks) - 1
    consecutive = 0

    for time in range(1, attacks[lastIdx][0] + 1):
        if attacks[idx][0] == time:
            answer -= attacks[idx][1]
            idx += 1

            if answer <= 0:
                return -1

            consecutive = 0
            continue

        answer = min(answer + bandage[1], health)

        consecutive += 1

        if consecutive == bandage[0]:
            answer = min(answer + bandage[2], health)
            consecutive = 0

    return answer

