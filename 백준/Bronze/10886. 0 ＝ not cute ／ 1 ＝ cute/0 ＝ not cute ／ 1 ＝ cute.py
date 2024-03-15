n = int(input())
iscute = []
for _ in range(n):
    iscute.append(input())

if iscute.count('0') > iscute.count('1'):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")