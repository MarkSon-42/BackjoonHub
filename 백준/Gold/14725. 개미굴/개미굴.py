# 트리에 새로운 가지를 추가하는 함수
def add_branch(tree, branch):
    # 가지가 비어있다면, 작업을 종료
    if not branch:
        return

    # 가지의 첫 번째 요소가 트리의 키가 아니라면,
    # 그것을 키로 하고 값은 빈 딕셔너리로 추가
    if branch[0] not in tree:
        tree[branch[0]] = {}

    # 가지의 나머지 부분에 대해 add_branch를 재귀적으로 호출
    # 새로운 트리 노드를 트리로 사용
    add_branch(tree[branch[0]], branch[1:])

# 트리를 출력하는 함수
def print_tree(tree, depth):
    # 트리의 각 키에 대해 (정렬된 순서로),
    # 깊이에 기반한 들여쓰기와 함께 출력
    # 그리고 그 키의 값 (하위 트리)에 대해 print_tree를 재귀적으로 호출, 깊이는 증가
    for key in sorted(tree.keys()):
        print("--" * depth + key)
        print_tree(tree[key], depth + 1)

# 사용자로부터 가지의 수를 받음
num_branches = int(input())

# 사용자로부터 가지를 받음
branches = [list(map(str, input().split())) for _ in range(num_branches)]

# 빈 트리를 초기화
tree = {}

# 각 가지를 트리에 추가
for branch in branches:
    # 가지의 첫 번째 요소는 가지 자체의 일부가 아니므로 건너뜀
    add_branch(tree, branch[1:])

# 트리를 출력
print_tree(tree, 0)