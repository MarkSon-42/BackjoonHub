# 세그먼트 트리 초기화 함수
def initialize(node, start, end):
    if start == end:
        seg[node] = 1
        return seg[node]
    seg[node] = initialize(node*2, start, (start+end)//2) + initialize(node*2 + 1, (start+end)//2+1, end)
    return seg[node]

# 세그먼트 트리에서 인덱스 찾는 함수
def find_index(node, start, end, value):
    if start == end:
        return start
    if value < seg[node*2 + 1]:
        return find_index(node*2 + 1, (start+end)//2 + 1, end, value)
    else:
        return find_index(node * 2, start, (start + end) // 2, value - seg[node * 2 + 1])

# 세그먼트 트리 업데이트 함수
def update_tree(node, start, end, index):
    if not (start <= index <= end):
        return
    seg[node] -= 1
    if start != end:
        update_tree(node*2, start, (start+end)//2, index)
        update_tree(node*2 + 1, (start+end)//2 + 1, end, index)

n = int(input())
sequence = list(map(int,input().split()))
seg = [0]*(4*n)
answer = [0]*n
initialize(1,0,n-1)
for i in range(n-1,-1,-1):
    index = find_index(1,0,n-1,sequence[i])
    answer[index] = i+1
    update_tree(1,0,n-1,index)
for i in answer:
    print(i, end=' ')