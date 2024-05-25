import heapq

def dijkstra(graph, start):
    # 初始化距离字典，用于存储从起点到每个节点的最短距离
    distance = {node: float('inf') for node in graph}
    distance[start] = 0  # 起点到自身的距离为0
    
    # 使用优先队列来存储节点及其对应的当前最短距离
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # 如果当前节点的距离大于已记录的距离，跳过
        if current_distance > distance[current_node]:
            continue
        
        # 遍历当前节点的邻居节点
        for neighbor, weight in graph[current_node].items():
            distance_to_neighbor = current_distance + weight
            # 如果通过当前节点到邻居节点的距离更短，更新距离字典
            if distance_to_neighbor < distance[neighbor]:
                distance[neighbor] = distance_to_neighbor
                heapq.heappush(pq, (distance_to_neighbor, neighbor))
    
    return distance

# 示例图
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print("从节点 {} 到各个节点的最短距离：".format(start_node))
for node, distance in shortest_distances.items():
    print("到节点 {}: 距离 {}".format(node, distance))
