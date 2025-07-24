import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 参数配置
num_turns = 10             # DNA螺旋圈数
points_per_turn = 100      # 每圈采样点数
radius = 1.0               # 螺旋半径
height = 3.4 * num_turns   # 总高度，DNA每圈高度约3.4nm
base_pair_step = 10        # 每多少点连一次碱基对

# t: 角度，z: 高度
t = np.linspace(0, 2 * np.pi * num_turns, num_turns * points_per_turn)
z = np.linspace(0, height, num_turns * points_per_turn)

# 链A（蓝色）
x1 = radius * np.cos(t)
y1 = radius * np.sin(t)

# 链B（红色，反向180度）
x2 = radius * np.cos(t + np.pi)
y2 = radius * np.sin(t + np.pi)

# 创建图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制主链
ax.plot(x1, y1, z, color='blue', label='Strand A')
ax.plot(x2, y2, z, color='red', label='Strand B')

# 绘制碱基对（连接两链）
for i in range(0, len(t), base_pair_step):
    ax.plot([x1[i], x2[i]], [y1[i], y2[i]], [z[i], z[i]], color='gray', alpha=0.6)

# 设置标签
ax.set_title("DNA Double Helix Structure", fontsize=16)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis (height)")
ax.legend()

plt.tight_layout()
plt.show()