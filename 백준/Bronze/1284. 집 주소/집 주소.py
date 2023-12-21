while True:
    answer = 2
    n = input()
    if n == "0":
        break
    for i in range(len(n)):
        if n[i] == "1":
            answer += 2
        elif n[i] == "0":
            answer += 4
        else:
            answer += 3

    answer += len(n) - 1

    print(answer)
