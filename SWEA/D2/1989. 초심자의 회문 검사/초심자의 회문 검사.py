
T = int(input())

for tc in range(1, T + 1):
    answer = 1
    s = input()
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            answer = 0
            break

    print(f'#{tc} {answer}')