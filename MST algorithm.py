import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    # 从未包含在 MST 中的顶点中，找到 key 值最小的顶点
    def min_key(self, key, mst_set):
        min_value = sys.maxsize
        for v in range(self.V):
            if key[v] < min_value and mst_set[v] == False:
                min_value = key[v]
                min_index = v
        return min_index

    # 使用 Prim's 算法找到最小生成树
    def prim_mst(self):
        key = [sys.maxsize] * self.V  # 用于保存顶点到 MST 的最小权值
        parent = [None] * self.V       # 用于保存 MST 中每个顶点的父节点
        key[0] = 0                     # 将起始顶点的 key 值设为 0，选中作为 MST 的起点
        mst_set = [False] * self.V     # 标记顶点是否包含在 MST 中

        parent[0] = -1                 # 起始顶点没有父节点

        for cout in range(self.V):
            # 选择 key 值最小的顶点 u，并将其标记为包含在 MST 中
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            # 更新与顶点 u 相邻的顶点的 key 值和父节点信息
            for v in range(self.V):
                if self.graph[u][v] > 0 and mst_set[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return parent

# 示例用法
g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

parent = g.prim_mst()

print("边 \t权值")
for i in range(1, g.V):
    print(parent[i], "-", i, "\t", g.graph[i][parent[i]])
