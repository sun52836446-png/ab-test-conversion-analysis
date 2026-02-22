import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.stats.proportion as sp
from scipy.stats import norm #引入norm模块，用于正态分布相关的统计计算


#1.获取数据集,查看前五行
data = pd.read_csv('C:\\Users\\86159\\Desktop\\data analysis\\ABtest\\ecommerce_ab_testing_2022_dataset1\\ab_data.csv')
data.head()

#查看数据行数，独立用户数
#print('数据行数:',data.shape[0])
#print('独立用户数:',data.user_id.nunique())

#筛选出来，出现过两次以上的用户，并进行排序
result = data[data.user_id.duplicated(keep=False)].sort_values(by='user_id').head(10)
print(result)

#存在对照组与实验组数据不匹配情况，例如treatment却对应了new_page，或者是control却对应成了old_page。
mismatch = ((data['group'] == 'treatment') != (data['landing_page'] == 'new_page'))
print('不匹配数量：',mismatch.sum())

#把符合的数据，单独创建一个副本
match_df = data[~mismatch].copy()
print('数据行数：', match_df.shape[0])
print('独立用户数：', match_df.user_id.nunique())

#a = match_df[match_df.user_id.duplicated(keep=False)]
#print(a)

match_df = match_df.drop_duplicates(subset = ['user_id'],keep = 'last')
print(match_df.isnull().sum())

#2.了解数据总体情况：多少条数据，多少个用户参与，测试时常
#新页面的用户占比
match_df[match_df.landing_page == "new_page"].shape[0]/match_df.shape[0]

#旧版，新版用户数
n_old = match_df.query('group == "control"').shape[0]
n_new = match_df.query('group == "treatment"').shape[0]
# 旧版、新版转化用户数
convert_old = match_df.query('group == "control"& converted == 1').shape[0]
convert_new = match_df.query('group == "treatment"& converted == 1').shape[0]
#旧版、新版转化率
p_old = convert_old/n_old
p_new = convert_new/n_new
print('旧版总受试用户数:', n_old, '旧版转化用户数:', convert_old, '旧版转化率:', p_old)
print('旧版总受试用户数:', n_new, '旧版转化用户数:', convert_new, '旧版转化率:', p_new)
#计算转化率的联合估计
p_c = (convert_old + convert_new)/(n_old+n_new)
print('联合转化率估计:',p_c)
#计算统计检验量z
z = (p_old - p_new)/ np.sqrt(p_c * (1-p_c) * (1/n_old + 1/n_new))
print('检验统计量：',z)

z_alpha = norm.ppf(0.05)
print('z_alpha:',z_alpha)

#计算Z值和P值
z_score, p_value = sp.proportions_ztest([convert_old, convert_new], [n_old, n_new], alternative='smaller')
print('检验统计量z:', z_score, ',p值:', p_value)
"""
检验统计量z: 1.3116075339133115 ,p值: 0.905173705140591
1. 统计结论（α=0.05）
p 值 = 0.90517 > 0.05 → 接受原假设；
结论：没有足够的统计证据证明 “新版转化率显著高于旧版”。
2. 业务结论
数值上：新版转化率略高于旧版，但这个提升是 “随机波动”，而非新版页面的真实效果；
行动建议：
不建议直接上线新版（无显著提升）；
无需否定新版（也无证据证明新版更差）；
可扩大测试样本量（样本越大，统计检验越灵敏，能检测到更小的真实差异）；
或分析新版的其他指标（如用户停留时长、点击次数），综合判断。
"""
