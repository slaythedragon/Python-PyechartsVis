import numpy as np
from pyecharts.charts import Bar
from pyecharts import options as opts


'''
2. 各岗位平均起薪柱状图
'''

# 1 读取数据
# 从publicFunction中导入read_works函数
from publicFunction import read_works
# 调用此函数，完成数据的读取和处理
data_cy = read_works()

# 2 计算各工作类别最低平均薪资
# 按照岗位类别分组来统计，根据起薪来计算平均值
work_salary = np.round(data_cy.groupby('岗位类别').mean()['起薪'])
# print(work_salary)


# 3. 绘图
# 去pyecharts-gallery网站找到模板示例
# https://gallery.pyecharts.org/#/Bar/bar_stack0
# 复制出来代码进行修改

# 实例化对象
p2obj = Bar()
# 将职位转化为列表形式作为x轴
p2obj.add_xaxis(work_salary.index.tolist())
# print(work_salary.index.tolist())

# 将最低平均薪资转化为列表形式作为y轴
p2obj.add_yaxis("各平均起薪", work_salary.tolist(),category_gap="50%")
# print(work_salary.tolist())
# 去pyecharts全局配置项中查参数
p2obj.set_global_opts(
    title_opts=opts.TitleOpts(title="不同岗位平均起薪"),
    # 让列的名字倾斜15度，负责有的名字太长，显示不出来
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15))
)

# 当这个程序有可能被导入时，写这个判断
# 直接用python程序调用当前这个脚本时，__name__为__main__，执行下面
# 当这个程序被导入时，__name__不为__main__，便不会执行
if __name__ == '__main__':
    # 生成页面
    p2obj.render('2.各岗位平均起薪柱状图.html')