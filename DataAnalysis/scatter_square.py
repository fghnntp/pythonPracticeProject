import matplotlib.pyplot as plt

x_values = [x for x in range(1, 1001)]
y_values = [x**2 for x in range(1, 1001)]
# edgecolors='none' 消除散点的边， s=40 圆点的大小用40
# RGB颜色 元组 c=c
c = (0, 0, 0.8)
# 颜色渐变 (colormap) 
plt.scatter(x_values, y_values, edgecolor='none', s=40, cmap=plt.cm.Blues) 
# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小, which='major' 指在刻度在中心的位置
plt.tick_params(axis='both', which='major', labelsize=14)
# 函数axis() 要求提供四个值：x 和 y 坐标轴的最小值和最大值
plt.axis([0, 1100, 0, 1100000])
# bbox_inches='tight' 保存没有边框的图形
plt.savefig('scater_square.png', bbox_inches='tight')
plt.show()