import random
import time

def subset_sum(masses, S):
    dp = [False] * (S + 1)
    dp[0] = True  # 0 можно получить, ничего не взяв
    prev = [None] * (S + 1)  # для восстановления пути

    for mass in masses:
        for s in range(S, mass - 1, -1):
            if dp[s - mass] and not dp[s]:
                dp[s] = True
                prev[s] = mass

    if not dp[S]:
        return False, []

    # Восстановление подмножества
    subset = []
    while S > 0:
        mass = prev[S]
        subset.append(mass)
        S -= mass

    return True, subset[::-1]  # по порядку

def average_runtime(k=20, max_mass=20, S=100, trials=10):
    total_time = 0
    for _ in range(trials):
        masses = [random.randint(1, max_mass) for _ in range(k)]
        start = time.perf_counter()
        found, subset = subset_sum(masses, S)
        end = time.perf_counter()
        total_time += end - start
    avg = total_time / trials
    print(f"Среднее время (k={k}, S={S}): {avg:.6f} сек")
    return avg

# График зависимости времени от суммы
import matplotlib.pyplot as plt

def plot_timings():
    ks = [10, 20, 30, 40, 50]
    Ss = [50, 100, 200, 300, 400]
    times = []
    for k, S in zip(ks, Ss):
        avg_time = average_runtime(k=k, S=S)
        times.append(avg_time)

    plt.plot(Ss, times, marker='o')
    plt.title("Время выполнения subset sum (O(S * k))")
    plt.xlabel("S (желаемая сумма)")
    plt.ylabel("Среднее время (сек)")
    plt.grid(True)
    plt.show()

plot_timings()
