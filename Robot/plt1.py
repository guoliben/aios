import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion()  # 开启交互模式

fig, ax = plt.subplots()
line, = ax.plot(np.random.randn(100))

for i in range(50):
    line.set_ydata(np.random.randn(100))  # 更新数据
    fig.canvas.draw()                     # 重绘画布
    fig.canvas.flush_events()             # 强制刷新
    time.sleep(0.1)                       # 等待
