import time


def find_median_sorted_arrays(nums1, nums2):
    # Гарантируем, что nums1 - это меньший массив
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)

    # Бинарный поиск по меньшему массиву
    left, right = 0, m
    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1

        # Взять элементы слева и справа от разделения
        max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float('inf') if partition1 == m else nums1[partition1]

        max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float('inf') if partition2 == n else nums2[partition2]

        if max_left1 <= min_right2 and max_left2 <= min_right1:
            # Нашли правильное разделение
            if (m + n) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            else:
                return max(max_left1, max_left2)
        elif max_left1 > min_right2:
            right = partition1 - 1
        else:
            left = partition1 + 1


def average_runtime(trials=10, nums1=None, nums2=None):
    if nums1 is None: nums1 = [1, 3, 8, 9, 15]
    if nums2 is None: nums2 = [7, 11, 19, 21, 18, 25]

    times = []

    for _ in range(trials):
        start = time.perf_counter()
        result = find_median_sorted_arrays(nums1, nums2)
        elapsed = time.perf_counter() - start
        times.append(elapsed)

    avg_time = sum(times) / trials
    print(f"Среднее время выполнения на {trials} запусков: {avg_time:.8f} секунд")
    print(f"Медиана: {result}")


# Пример вызова
average_runtime()

