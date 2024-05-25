class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    # 添加边
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # 深度优先搜索
    def dfs(self, u, visited):
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self.dfs(v, visited)

    # 检查图是否连通
    def is_connected(self):
        visited = [False] * self.V

        # 找到第一个非空的顶点作为起点
        for i in range(self.V):
            if len(self.graph[i]) > 0:
                start = i
                break

        self.dfs(start, visited)

        # 检查所有顶点是否都被访问到
        for i in range(self.V):
            if visited[i] == False and len(self.graph[i]) > 0:
                return False

        return True

    # 辅助函数：欧拉路径
    def euler_util(self, u, visited):
        for v in self.graph[u]:
            if self.is_valid_next_edge(u, v, visited):
                print(u, "->", v)
                visited[v] = True
                self.euler_util(v, visited)

    # 辅助函数：检查下一条边是否合法
    def is_valid_next_edge(self, u, v, visited):
        if len(self.graph[u]) == 1:
            return True

        visited_vertices = 0
        for i in self.graph[u]:
            if visited[i]:
                visited_vertices += 1
        if visited_vertices == len(self.graph[u]):
            return True

        visited[u] = True
        count1 = self.dfs_count(u, visited)

        self.graph[u].remove(v)
        self.graph[v].remove(u)

        visited = [False] * self.V
        count2 = self.dfs_count(u, visited)

        self.graph[u].append(v)
        self.graph[v].append(u)

        return False if count1 > count2 else True

    # 辅助函数：计算从给定顶点开始的连通分量大小
    def dfs_count(self, u, visited):
        count = 1
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                count = count + self.dfs_count(v, visited)
        return count

    # Fleury 算法主函数
    def fleury(self):
        if not self.is_connected():
            print("图不连通！")
            return

        odd_degree = 0
        start_vertex = 0
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                odd_degree += 1
                start_vertex = i

        if odd_degree > 2:
            print("无欧拉回路！")
            return

        print("欧拉回路：")
        self.euler_util(start_vertex, [False] * self.V)


# 示例用法
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

g.fleury()
