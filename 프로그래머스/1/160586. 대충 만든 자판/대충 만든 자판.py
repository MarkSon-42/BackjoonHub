def solution(keymap, targets):
    result = []

    exist_char = {}
    
    # key별 최소 key press 수 정리
    for key_arr in keymap:
        for i in range(len(key_arr)):
            key = key_arr[i]
            exist_char[key] = min(exist_char.get(key, 99999999), i + 1)
    
    for target in targets:
        cnt = 0
        for char in target:
            if char not in exist_char:
                cnt = -1
                break
            else:
                cnt += exist_char[char]
        result.append(cnt)
    
    return result
