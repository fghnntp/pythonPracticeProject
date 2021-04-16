import matplotlib.pyplot as plt
# 快捷键
# o 放大
# p 移动标
# c 上一个视图
# v 下一个视图
# h 回到最初始化视图

# SimHei	        中文黑体
# Kaiti	            中文楷体
# LiSu	            中文隶书
# FangSong	        中文仿宋
# YouYuan	        中文幼圆
# STSong	        华文宋体
# Microsoft YaHei   微软雅黑
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

input_value = [x for x in range(100)]
squares = [x**2 for x in range(100)]
# linewidth 画线的宽度
plt.plot(squares, linewidth=3) 
# 标题字体大小
plt.title('Square Number', fontsize=24)
# x轴标签字体的大小
plt.xlabel('值', fontsize=14)
# y轴标签字体的大小
plt.ylabel('Square of Value', fontsize=14)
# 刻度的样式，axis='both'代表刻度的样式会影响所有的轴
# 刻度标签的字体大小位14
plt.tick_params(axis='both', labelsize=14)
plt.show()