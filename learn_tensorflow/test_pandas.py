# -*- coding: utf-8 -*-

import pandas as pd

print pd.__version__

# DataFrame 关系型数据表格 包含多个行和已命名的列
# Series 单一列

city_names = pd.Series(["San Francisco", "San Jose", "Sacramento"])
population = pd.Series([852469, 1015785, 485199])
# 生成 一个表格
pd.DataFrame({"City Name": city_names, "Population": population})

# 加载 csv 数据
california_house_dataframe = pd.read_csv('california_housing_train.csv', sep=',')
# 简单常用的统计信息
california_house_dataframe.describe()
# 显示前几行
california_house_dataframe.head()
# 显示后几行
print california_house_dataframe.tail(5)
# 绘制图表
california_house_dataframe.hist("housing_median_age")
