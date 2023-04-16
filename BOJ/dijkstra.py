import heapq

INF = int(1e9)

def dijkstra(array, start):
    distance = {node: INF for node in array}
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for next_dist, next in array[node].items():
            new_dist = next_dist + dist
            if new_dist < distance[next]:
                distance[next] = new_dist
                heapq.heappush(queue, [new_dist, next])
    return distance