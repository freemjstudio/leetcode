# 최소 신장 트리 찾기

# 사이클을 확인하는 함수
# -> 노드들의 부모 노드가 같으면 사이클 발생
# -> 노드들의 부모 노드가 다르면 사이클 없음

# 자기 자신을 부모노드로 초기화 함

v, e = map(int, input().split())
parents = [i for i in range(1, v+1)]
edges = []
total_cost = 0
def find_parent(x, parents):
    if parents[x] != x:
        parents[x] = find_parent(parents[x], parents)
    return parents[x]

def union_parent(parents, a, b):
    a = find_parent(a, parents)
    b = find_parent(b, parents)
    if a < b:
        parents[b] = a # 숫자 작은 것을 더 상위 노드라고 가정
    else:
        parents[a] = b

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

# 간선 정보를 확인하면서 최소 신장 트리를 찾음
for i in range(e):
    cost, a, b = edges[i]
    if find_parent(a, parents) != find_parent(b, parents):
        union_parent(parents, a, b)
        total_cost += cost
print(total_cost)
