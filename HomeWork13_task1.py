import time
from collections import defaultdict
import random


# Класс графа
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    # Добавление ребра (неориентированный граф)
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Обход в глубину
    def dfs(self, v, visited):
        visited[v] = True
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                self.dfs(neighbour, visited)

    def full_dfs(self):
        visited = [False] * self.V
        for v in range(self.V):
            if not visited[v]:
                self.dfs(v, visited)


# Генерация случайного неориентированного графа
def generate_random_graph(n_nodes, n_edges):
    g = Graph(n_nodes)
    edges = set()
    while len(edges) < n_edges:
        u = random.randint(0, n_nodes - 1)
        v = random.randint(0, n_nodes - 1)
        if u != v and (u, v) not in edges and (v, u) not in edges:
            g.add_edge(u, v)
            edges.add((u, v))
    return g


# Тестирование времени выполнения
import matplotlib.pyplot as plt

node_sizes = [100, 500, 1000, 2000, 3000, 5000, 7000, 10000]
times = []

for n in node_sizes:
    e = n * 2  # средняя плотность
    g = generate_random_graph(n, e)

    start = time.perf_counter()
    g.full_dfs()
    end = time.perf_counter()

    duration = end - start
    times.append(duration)
    print(f"V={n}, E={e}, Время: {duration:.6f} сек")

# Построение графика
plt.figure(figsize=(10, 5))
plt.plot(node_sizes, times, marker='o')
plt.title("Зависимость времени DFS от количества вершин")
plt.xlabel("Количество вершин (V)")
plt.ylabel("Время выполнения (сек)")
plt.grid(True)
plt.show()
