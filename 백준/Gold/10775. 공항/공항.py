def find_gate(gate):
    if parent[gate] < 0:
        return gate
    parent[gate] = find_gate(parent[gate])
    return parent[gate]

def union_gate(root, gate):
    root, gate = find_gate(root), find_gate(gate)
    if root != gate:
        parent[gate] = root


num_gates, num_planes = int(input()), int(input())
global parent
parent = [-1 for _ in range(num_gates + 1)]
num_landed = 0
for _ in range(num_planes):
    plane = int(input())
    target_gate = find_gate(plane)
    if target_gate == 0:
        break
    union_gate(target_gate - 1, target_gate)
    num_landed += 1
print(num_landed)
