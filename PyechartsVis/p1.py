import numpy as np
from pyecharts.charts import Pie
from pyecharts import options as opts

'''
1. 各岗位占比饼图
'''

# 1 读取数据
# 从publicFunction中导入read_works函数
from publicFunction import read_works
# 调用此函数，完成数据的读取和处理
data_cy = read_works()

# 2 统计不同岗位数量
# 按照岗位类别分组来统计，根据岗位id来计数
work_count = data_cy.groupby('岗位类别').count()['岗位id']
#print(work_count)

# 3 计算岗位占比
# 算出work_count/work_count.sum())*100算出百分比，np.round( ,2)保留小数点后两位
work_ratio = np.round((work_count/work_count.sum())*100,2)
# print(work_ratio)


# 去pyecharts网站找到饼图模板
# https://pyecharts.org/#/zh-cn/basic_charts?id=pie%ef%bc%9a%e9%a5%bc%e5%9b%be
# 要求的系列数据项，格式为 [(key1, value1), (key2, value2)]，所以要进行数据的组合

# 组合数据
#
# work_ratio.index.tolist()即岗位类别的名称
# print(work_ratio.index.tolist())
# *zip进行数据的组合压缩,再和占比放到一个列表中
work_name_ratio = [*zip(work_ratio.index.tolist(),work_ratio)]
# print(work_name_ratio)
# [('java', 5.94), ('python', 6.75), ('产品助理', 6.57), ('人事', 6.66), ...]


# 4 绘图
# 实例化对象
p1obj = Pie()
# 放入组合数据
# radius为饼图的半径，数组的第一项是内半径，第二项是外半径
p1obj.add('',work_name_ratio,radius=["40%", "75%"],)
# 去pyecharts全局配置项中查参数
# https://pyecharts.org/#/zh-cn/global_options?id=legendopts%ef%bc%9a%e5%9b%be%e4%be%8b%e9%85%8d%e7%bd%ae%e9%a1%b9
p1obj.set_global_opts(
    # 标题
    title_opts=opts.TitleOpts(title="各岗位占比"),
    # orient图例列表的布局朝向为竖着，离上方15%，离左边2%
    legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%")
)
# b代表给的数据中的key，c代表给的数据中value，c的后面加百分号
p1obj.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))

# 当这个程序有可能被导入时，写这个判断
# 直接用python程序调用当前这个脚本时，__name__为__main__，执行下面
# 当这个程序被导入时，__name__不为__main__，便不会执行
if __name__ == '__main__':
    #     # 生成页面
    p1obj.render('1.各岗位占比饼图.html')
