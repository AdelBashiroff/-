import time
import random
from collections import defaultdict, deque

class DAG:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.in_degree = [0] * V

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.in_degree[v] += 1

    def topological_sort(self):
        in_deg = self.in_degree[:]
        queue = deque([v for v in range(self.V) if in_deg[v] == 0])
        result = []

        while queue:
            u = queue.popleft()
            result.append(u)
            for v in self.graph[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    queue.append(v)

        return result if len(result) == self.V else []

    def has_hamiltonian_path(self):
        topo = self.topological_sort()
        if not topo:
            return False
        for i in range(len(topo) - 1):
            if topo[i + 1] not in self.graph[topo[i]]:
                return False
        return True

def average_runtime_dag(trials=10, size=1000):
    total = 0
    for _ in range(trials):
        dag = DAG(size)
        # Строим цепочку (гарантированный Гамильтонов путь)
        for i in range(size - 1):
            dag.add_edge(i, i + 1)
        # Случайно добавим дополнительные ребра, не нарушая ацикличность
        for _ in range(size // 2):
            u = random.randint(0, size - 2)
            v = random.randint(u + 1, size - 1)
            dag.add_edge(u, v)
        start = time.perf_counter()
        _ = dag.has_hamiltonian_path()
        end = time.perf_counter()
        total += (end - start)
    print(f"Среднее время: {total / trials:.6f} сек при {size} вершинах")

# Пример запуска
average_runtime_dag()
