from pyecharts.charts import HeatMap
from pyecharts import options as opts


'''
4. 各城市岗位薪资分布热力图
'''

# 1 读取数据
# 从publicFunction中导入read_works函数
from publicFunction import read_works
# 调用此函数，完成数据的读取和处理
data_cy = read_works()

# 2 统计数据
# 生成城市为行索引，工作类别为列索引，薪资为表格值的透视表。
city_data = data_cy.pivot_table(index=['城市'], columns=['岗位类别'], aggfunc={'最高薪资': 'mean'})
# 按‘python’列对透视表进行降序排列，ascending 升序
city_data.sort_values([('最高薪资', 'python')], ascending=False, inplace=True, na_position='last')
# print(city_data)
# 取前20个最高薪资
top_city = city_data[:20]['最高薪资']
# print(top_city)

# 做成数据透视表进行绘图
values = [[item_col, item_index, round(top_city.iloc[item_index, item_col], 2)] for item_col in range(len(top_city.columns)) for item_index in range(len(top_city.index))]
# print(top_city.index.tolist())#行名
# print(top_city.columns.tolist())#列名
# print(values)#[行坐标，列坐标，薪资]

# 3 绘图
# InitOpts(width="1200px", height="800px")设置图的宽高
p4obj = HeatMap(init_opts=opts.InitOpts(width="1200px", height="800px"))
p4obj.add_xaxis(top_city.columns.tolist())
p4obj.add_yaxis("平均最高薪资", top_city.index.tolist(), values,label_opts=opts.LabelOpts(is_show=True, position="inside"),)
p4obj.set_global_opts(
    title_opts=opts.TitleOpts(title="各城市岗位薪资分布热力图"),
    visualmap_opts=opts.VisualMapOpts(min_=5000, max_=50000),
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15))
)

# 当这个程序有可能被导入时，写这个判断
# 直接用python程序调用当前这个脚本时，__name__为__main__，执行下面
# 当这个程序被导入时，__name__不为__main__，便不会执行
if __name__ == '__main__':
    p4obj.render("4.各城市岗位薪资分布热力图.html")