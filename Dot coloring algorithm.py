class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    # 添加边
    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    # 输出着色结果
    def print_colors(self, colors):
        for v in range(self.V):
            print("顶点 {} 被着色为颜色 {}".format(v, colors[v]))

    # 着色函数
    def greedy_coloring(self):
        # 初始化所有顶点的颜色为无色（-1）
        colors = [-1] * self.V

        # 将第一个顶点着色为第一个颜色（0）
        colors[0] = 0

        # 为剩余的顶点着色
        for v in range(1, self.V):
            # 初始化该顶点的可用颜色集合为所有颜色
            available_colors = [True] * self.V

            # 检查与该顶点相邻的顶点已经着色的情况
            for u in range(self.V):
                if self.graph[v][u] == 1 and colors[u] != -1:
                    available_colors[colors[u]] = False

            # 找到第一个可用的颜色并着色
            for color in range(self.V):
                if available_colors[color]:
                    colors[v] = color
                    break

        # 输出着色结果
        self.print_colors(colors)


# 示例用法
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("点着色算法结果：")
g.greedy_coloring()
