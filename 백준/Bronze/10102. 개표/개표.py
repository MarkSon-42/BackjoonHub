V = int(input())
a_cnt = 0
b_cnt = 0
s = input()
for c in s:
    if c == 'A':
        a_cnt += 1
    else:
        b_cnt += 1

if a_cnt > b_cnt:
    print('A')
elif a_cnt < b_cnt:
    print('B')
else:
    print('Tie')