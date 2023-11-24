t = int(input())

for tc in range(1, t + 1):
    input_str = input()
    pattern = ""
    for i in range(1, len(list(input_str))):
        pattern = input_str[:i]

        if input_str[i : i + len(list(pattern))] == pattern:
            print(f"#{tc} {len(pattern)}")
            break
