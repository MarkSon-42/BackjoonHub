n = int(input())
s = input()
dict_list = {
    '000000': 'A',
    '001111': 'B',
    '010011': 'C',
    '011100': 'D',
    '100110': 'E',
    '101001': 'F',
    '110101': 'G',
    '111010': 'H'
    }

def func():
    answer = ''
    for i in range(n):
        sep = s[6 * i : 6 * (i + 1)]
        for k, v in dict_list.items():
            cnt = 0
            for a, b in zip(k, sep):
                if a != b:
                    cnt += 1
            if cnt < 2:
                answer += v
                break
        else:
            return i + 1
    return answer

print(func())