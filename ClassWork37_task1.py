import random
import time
from collections import defaultdict

# Структура графа
class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def find_mother_vertex(self):
        visited = [False] * self.V
        last_v = 0

        for v in range(self.V):
            if not visited[v]:
                self.dfs_util(v, visited)
                last_v = v

        # Проверим, действительно ли last_v — кандидат
        visited = [False] * self.V
        self.dfs_util(last_v, visited)
        if all(visited):
            return last_v
        return -1  # Такой вершины нет

def average_runtime_graph(trials=10, size=1000):
    total_time = 0
    for _ in range(trials):
        g = Graph(size)
        # Случайный сильно связанный граф + добавим связи
        for _ in range(size * 3):
            u = random.randint(0, size - 1)
            v = random.randint(0, size - 1)
            if u != v:
                g.add_edge(u, v)
        start = time.perf_counter()
        _ = g.find_mother_vertex()
        end = time.perf_counter()
        total_time += (end - start)
    avg = total_time / trials
    print(f"Среднее время: {avg:.6f} сек при {size} вершинах")

# Пример запуска
average_runtime_graph()
