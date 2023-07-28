from built_modules.import_number_system_converter import convertNum
import matplotlib.pyplot as plt, numpy as np

n = 10
# rng = 5

def f(n: int, l_max: int, r_max: int, x: int = 0):
    s = 0
    if n:
        if l_max < x <= r_max:
            s += f(n - 1, l_max, r_max, x - 1)
        if l_max <= x < r_max:
            s += f(n - 1, l_max, r_max, x + 1)
        return s
    else:
        return 1

# for i in range(rng): # 0, 1, 2, 3, 4 (rng = 5)
#     # if not(i):
#     #     print(f(4, i - rng + 1, i) - f(4, i - rng + 2, i)) # (-4, 0), (-3, 1), (-2, 2), (-1, 3), (0, 4) (rng = 5)
#     # elif i + 1 == rng:
#     #     print(f(4, i - rng + 1, i) - f(4, i - rng + 1, i - 1))
#     # else:
#     #     print(f(4, i - rng + 1, i) - f(4, i - rng + 2, i - 1))
#     print(f(4, i - rng + 1, i) - f(4, i - rng + 2, i) - f(4, i - rng + 1, i - 1) + f(4, i - rng + 2, i - 1))

n_max = 20

average_ranges = []
ranges_lst = []
for i in range(n_max):
    for j in range(i + 2):
        ranges_lst.append(0)

    for j in range(2 ** i):
        num = convertNum(str(j), 10, 2, i)
        pos = 0
        x_min = 0
        x_max = 0
        for k in num:
            pos += 2 * int(k) - 1
            x_min = min(pos, x_min)
            x_max = max(pos, x_max)
        ranges_lst[x_max - x_min + 1] += 1
    average_ranges.append(np.average(range(len(ranges_lst)), weights = ranges_lst))
    ranges_lst.clear()

print(average_ranges)
plt.plot(range(n_max), average_ranges)
plt.show()