#c использованием numpy
import numpy as np
import time
import random
N, M = 1000, 1000
random.seed(0)
A_list = np.random.randint(0, 100, size=(N, M))
start = time.time()
row_means_up = A_list.mean(axis=1)
max_mean_up = row_means_up.max()
end = time.time()
print(max_mean_up, end)

#без использования numpy
N, M = 1000, 1000
random.seed(0)
A_list = [[random.randint(0, 99) for _ in range(M)] for _ in range(N)]
start = time.time()
row_means_up = [sum(row) / len(row) for row in A_list]
max_mean_up = max(row_means_up)
end = time.time()
print(max_mean_up, end)