# https://school.programmers.co.kr/learn/courses/30/lessons/42861

def solution(n, costs):
    answer = 0 # total cost
    # 자기 자신을 부모 노드로 초기화
    parent = [i for i in range(n)]

    def find_parent(x, parent):
        if parent[x] != x:
            parent[x] = find_parent(parent[x], parent)
        return parent[x]

    def union_parent(a, b, parent):
        a = find_parent(a, parent)
        b = find_parent(b, parent)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    edges = []
    for a, b, cost in costs:
        edges.append((cost, a, b))
    edges.sort()

    for edge in edges:
        cost, start, end = edge
        if find_parent(start, parent) != find_parent(end, parent):
            union_parent(start, end, parent)
            answer += cost

    return answer