# import numpy as np

n = int(input())
# x = np.arange(n)
x = []

# 入力値を配列に代入
for i in range(n):
    R = int(input())
    x.append(R)

# 最大利益
# 十分小さい値を初期値に設定
maxv = -20000000000

# 最小値
minv = x[0]

z = 1

for j in range(n-1):
    maxv = max(maxv, x[z] - minv)
    minv = min(minv, x[z])

    z += 1
print(maxv)
