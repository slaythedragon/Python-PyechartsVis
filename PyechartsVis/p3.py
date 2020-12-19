import pandas as  pd
import numpy as np
from pyecharts.charts import Bar,Line
from pyecharts import options as opts


'''
3.各城市招聘量柱状图及平均薪资折线图组合
'''

# 1 读取数据
# 从publicFunction中导入read_works函数
from publicFunction import read_works
# 调用此函数，完成数据的读取和处理
data_cy = read_works()
# 只拿出数据科学的岗位进行分析
data_cy = data_cy[data_cy['岗位类别'] == '数据科学'].copy()

# 2 统计城市招聘数据
# 按照城市分组来统计数量，根据岗位id来计数,进行降序排列
city_nums = data_cy.groupby('城市').count()['岗位id'].sort_values(ascending=False)
# print(city_nums)

# 要将城市对应的招聘量(用柱状图)和平均薪资(用折线图)放在一起展示

# 3 计算对应城市的平均薪资（按起薪资计算平均值）
# 按照城市分组来统计数量，根据起薪来计算平均值
data_city = np.round(data_cy.groupby('城市').mean()['起薪'])
# print(data_cy.groupby('城市').mean())

# 取招聘量前10个的城市的平均起薪
city_salary = data_city.loc[city_nums[:10].index.tolist()]
# print(city_salary)

# 4 绘图，要将城市对应的招聘量(用柱状图)和平均薪资(用折线图)放在一起展示
# 根据pyecharts-gallery中的示例来改
# https://gallery.pyecharts.org/#/Bar/multiple_y_axes
p3obj = (
    # 城市对应的招聘量的柱状图
    Bar()
    # 取招聘量前10的城市
    .add_xaxis(xaxis_data=city_nums[:10].index.tolist())
    .add_yaxis(
        series_name="招聘量",
        yaxis_data=city_nums[:10].tolist(),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="薪资",
            type_="value",
            # 薪资y坐标最低10000，最高20000
            min_=10000,
            max_=20000,
            # interval=500,
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
        )
    )
    # 去pyecharts全局配置项中查参数
    .set_global_opts(
        title_opts=opts.TitleOpts(title="招聘与薪资排行榜"),
        tooltip_opts=opts.TooltipOpts(
            is_show=True, trigger="axis", axis_pointer_type="cross"
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
        ),
        # 招聘数量y坐标最低0，最高1500
        yaxis_opts=opts.AxisOpts(
            name="数量",
            type_="value",
            min_=0,
            max_=1500,
            # interval=50,
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
)
# 画出平均薪资的折线
line = (
    Line()
    .add_xaxis(xaxis_data=city_nums[:10].index.tolist())
    .add_yaxis(
        series_name="平均薪资",
        yaxis_index=1,
        y_axis=city_salary,
        label_opts=opts.LabelOpts(is_show=False),
    )
)

# 当这个程序有可能被导入时，写这个判断
# 直接用python程序调用当前这个脚本时，__name__为__main__，执行下面
# 当这个程序被导入时，__name__不为__main__，便不会执行
if __name__ == '__main__':
    # 生成页面，表示柱状图里面套着线图
    p3obj.overlap(line).render("3.各城市招聘量柱状图及平均薪资折线图组合.html")