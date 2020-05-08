import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# plt.style.use('seaborn')  # 更换图像样式
plt.rcParams['font.family'] = ['Arial Unicode MS', 'Microsoft Yahei', 'SimHei', 'sans-serif']  # 解决中文乱码
# plt.rcParams['axes.unicode_minus'] = False  # 如果字体为SimHei黑体,负号乱码,解决

# MAC电脑解决图片模糊魔术命令
# %config InlineBackend.figure_format = 'retina'
delta = (datetime.datetime.now() - start).total_seconds()