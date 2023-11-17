for i in range(1,11):
    num=int(input())
    a=list(map(int,input().split()))
 
    for _ in range(num):
        a.sort()
        a[0]+=1
        a[-1]-=1
 
    print(f'#{i} {max(a)-min(a)}')
