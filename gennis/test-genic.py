import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置参数
num_turns = 10             # 螺旋圈数
points_per_turn = 100      # 每圈的点数
height = 15                # 总高度
radius = 1.0               # 螺旋半径
base_pair_step = 10        # 每几个点绘制一次碱基对连接线

# 构造螺旋参数 t
t = np.linspace(0, 2 * np.pi * num_turns, num_turns * points_per_turn)
z = np.linspace(0, height, num_turns * points_per_turn)

# 两条反相的螺旋链
x1 = radius * np.cos(t)
y1 = radius * np.sin(t)

x2 = radius * np.cos(t + np.pi)
y2 = radius * np.sin(t + np.pi)

# 创建图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x1, y1, z, color='blue', label='Strand A')
ax.plot(x2, y2, z, color='red', label='Strand B')

# 添加连接线（模拟碱基对）
for i in range(0, len(t), base_pair_step):
    ax.plot([x1[i], x2[i]], [y1[i], y2[i]], [z[i], z[i]], color='gray', alpha=0.6)

# 设置图形属性
ax.set_title("DNA Double Helix", fontsize=16)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()

plt.tight_layout()
plt.show()