class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_edge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def dfs(self, u, visited):
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self.dfs(v, visited)

    def is_connected(self):
        visited = [False] * self.V
        for i in range(self.V):
            if len(self.graph[i]) > 0:
                start = i
                break
        self.dfs(start, visited)
        for i in range(self.V):
            if visited[i] == False and len(self.graph[i]) > 0:
                return False
        return True

    def is_valid_next_edge(self, u, v):
        if len(self.graph[u]) == 1:
            return True
        visited = [False] * self.V
        count1 = self.dfs_count(u, visited)
        self.remove_edge(u, v)
        visited = [False] * self.V
        count2 = self.dfs_count(u, visited)
        self.add_edge(u, v)
        return True if count1 <= count2 else False

    def dfs_count(self, u, visited):
        count = 1
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                count = count + self.dfs_count(v, visited)
        return count

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
            print("无欧拉路径！")
            return
        current_vertex = start_vertex
        while len(self.graph[current_vertex]) > 0:
            for v in self.graph[current_vertex]:
                if self.is_valid_next_edge(current_vertex, v):
                    print(current_vertex, "-", v)
                    self.remove_edge(current_vertex, v)
                    current_vertex = v
                    break
        print("Fleury算法找到的欧拉路径已完成！")

# 示例用法
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

print("使用Fleury算法找到的欧拉路径：")
g.fleury()
