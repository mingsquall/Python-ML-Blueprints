# 在这里做一些准备工作 :) 然后在Jupyter中使用 from pre_import import * 就可以愉快的py了
# -*- coding: utf-8 -*-
import os
import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

# 获取数据：使用Requests下载数据集iris.data
PATH = r'/Users/patientman/Desktop/iris'
r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
# 准备数据文件
with open(PATH + '/iris.data', 'w') as f:
    f.write(r.text)
os.chdir(PATH)
# 读取CSV数据文件，并增加列名，生成DataFrame
df = pd.read_csv(PATH + '/iris.data', names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])

import seaborn as sns