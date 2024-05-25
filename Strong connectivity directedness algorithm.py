from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # 辅助函数：在 DFS 中递归访问节点
    def dfs_util(self, u, visited, stack):
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self.dfs_util(v, visited, stack)
        stack.append(u)

    # 获取转置图
    def get_transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # 主函数：查找强连通分量
    def get_scc(self):
        stack = []
        visited = [False] * self.V

        # 第一次 DFS，将顶点按完成时间存入栈中
        for i in range(self.V):
            if not visited[i]:
                self.dfs_util(i, visited, stack)

        # 获取转置图
        transpose_graph = self.get_transpose()

        # 清空访问数组
        visited = [False] * self.V

        # 第二次 DFS，从栈中弹出节点，获取强连通分量
        scc_list = []
        while stack:
            i = stack.pop()
            if not visited[i]:
                scc = []
                transpose_graph.dfs_util(i, visited, scc)
                scc_list.append(scc)

        return scc_list

# 示例用法
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

scc = g.get_scc()
print("强连通分量为：", scc)
