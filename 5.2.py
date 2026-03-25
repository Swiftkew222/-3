import random
import statistics
import math
N = [random.randint(1, 100) for _ in range(100)]
mean_1 = statistics.mean(N)
median_1 = statistics.median(N)
stdev_1 = statistics.stdev(N)
sum_n = sum(N)
square_root = round(math.sqrt(sum_n), 2)
print(f"Среднее: {mean_1:.2f}, Медиана: {median_1:.2f}, Стандартное отклонение: {stdev_1:.2f},Корень из суммы: {square_root}")
