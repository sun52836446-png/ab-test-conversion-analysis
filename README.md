# ab-test-conversion-analysis
A/B testing analysis of e-commerce landing page conversion using statistical hypothesis testing and data cleaning workflow.

 电商落地页 A/B 测试分析项目
 项目简介

本项目通过对电商平台落地页改版前后进行 A/B 测试分析，验证新版页面是否能够显著提升用户转化率。项目完整覆盖实验设计、数据清洗、统计检验与业务决策输出流程，模拟真实企业数据分析场景，体现数据驱动产品优化决策的方法论。

 项目目标

验证新版落地页转化率是否显著高于旧版页面，从统计与业务双维度判断页面改版上线的可行性。

 实验设计
分组	页面版本	说明
Control	旧版页面	原始页面设计
Treatment	新版页面	优化后的布局与交互

核心指标

转化率 = 转化用户数 / 参与用户数

随机分组原则

用户随机分流至实验组与对照组，保证样本独立性与实验公平性。

 数据清洗流程

为保证实验结果可信性，对原始数据进行了系统清洗：

移除实验污染样本（分组与页面不一致）

去除重复用户记录（保留最后一次访问）

检查缺失值与异常数据

 核心结果
版本	用户数	转化数	转化率
旧版	n_old	convert_old	p_old
新版	n_new	convert_new	p_new

转化率差值：

p_new − p_old
 统计检验方法

采用 双样本比例 Z 检验 判断转化率差异显著性。

假设设定

H0: p_old ≥ p_new
H1: p_old < p_new
α = 0.05

检验工具

statsmodels.stats.proportion.proportions_ztest
 检验结果

Z值：1.3116

P值：0.9052

统计结论

P > 0.05，无法拒绝原假设
新版页面未显著提升转化率

 业务结论

新版页面提升幅度较小且不具统计显著性

当前证据不足以支持上线新版页面

本次结果可能来自随机波动而非真实效果

 优化建议

扩大样本量提高检验灵敏度

对新版页面进行进一步交互优化

 技术栈
Python
Pandas
NumPy
Statsmodels

分用户群体开展分层实验

引入辅助指标（停留时长、跳出率等）综合评估
