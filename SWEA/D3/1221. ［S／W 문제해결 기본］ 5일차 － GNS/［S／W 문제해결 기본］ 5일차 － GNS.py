T = int(input())
numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
dic = {numbers[i]: i for i in range(10)}
for tc in range(1, T+1):
    _, length = input().split()
    length = int(length)
    words = input().split()
    words.sort(key=lambda x: dic[x])
    print(f'#{tc} {" ".join(words)}')