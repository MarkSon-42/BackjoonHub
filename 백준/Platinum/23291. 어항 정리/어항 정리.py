def adjust(arr):
    narr = [x[:] for x in arr]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni,nj=i+di,j+dj
                if 0<=ni<len(arr) and 0<=nj<len(arr[ni]) and arr[i][j]>arr[ni][nj]:
                    d = (arr[i][j]-arr[ni][nj])//5
                    if d>0:
                        narr[i][j]-=d
                        narr[ni][nj]+=d
    return narr

def flatten(arr):
    narr=[]
    for j in range(len(arr[-1])):
        for i in range(len(arr)-1,-1,-1):
            if j<len(arr[i]):
                narr.append(arr[i][j])
    return narr

N, K = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
while max(arr)-min(arr)>K:
    mn = min(arr)
    for i in range(len(arr)):
        if arr[i]==mn:
            arr[i]+=1

    arr = [[arr[0]]]+[arr[1:]]
    while True:
        w=len(arr[-2])
        if len(arr)>len(arr[-1])-w:
            break
        arr1 = [lst[:w] for lst in arr]
        arr2 = list(map(list,zip(*arr1[::-1])))
        arr = arr2 + [arr[-1][w:]]

    narr = adjust(arr)
    arr = flatten(narr)

    M = len(arr)//2
    narr=[arr[:M][::-1]]+[arr[M:]]
    M = M//2
    arr1 = [lst[:M] for lst in narr]
    arr = [lst[::-1] for lst in arr1[::-1]] + [lst[M:] for lst in narr]

    narr = adjust(arr)
    arr=flatten(narr)

    ans+=1
print(ans)