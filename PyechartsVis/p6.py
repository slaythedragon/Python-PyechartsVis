from pyecharts.charts import Bar,Page
from pyecharts import options as opts

'''
6.不同岗位对学历和工作经验要求分布柱状图
'''

# 读取数据
# 从publicFunction中导入read_works函数
from publicFunction import read_works
# 调用此函数，完成数据的读取和处理
data_cy = read_works()


# 不同岗位对学历要求分布柱状图

# 统计学历要求数据
# 按照岗位类别、学历要求分组来统计数量，根据岗位id来计数
data_gr = data_cy.groupby(['岗位类别', '学历要求']).count()['岗位id']  # 计算各种学历在每个岗位类别中所对应的岗位数量
# print(data_gr)

xindex = ['不限','大专','本科','硕士','博士']

# 选取工作类别‘java’、‘python’、‘数据科学’、‘算法工程师’所对应的数据，画出不同岗位对学历要求分布柱状图
p6obj1 = Bar()
p6obj1.add_xaxis(xindex)
p6obj1.add_yaxis("java", list(data_gr['java'].reindex(xindex)), gap="0%")
p6obj1.add_yaxis("python", list(data_gr['python'].reindex(xindex)), gap="0%")
p6obj1.add_yaxis("数据科学", list(data_gr['数据科学'].reindex(xindex)), gap="0%")
p6obj1.add_yaxis("算法工程师", list(data_gr['算法工程师'].reindex(xindex)), gap="0%")
p6obj1.set_global_opts(title_opts=opts.TitleOpts(title="不同岗位对学历要求分布柱状图"))



# 不同岗位对工作经验要求分布柱状图

# 统计对应工作经验数据
# 按照岗位类别、工作年限分组来统计数量，根据岗位id来计数
data_gr1 = data_cy.groupby(['岗位类别', '工作年限']).count()['岗位id']  # 计算每个岗位类别中相同工作年限的要求的数量
# print(data_gr1)
yindex = ['不限','在校/应届','1年以下','1-3年','3-5年','5-10年','10年以上']


# 选取工作类别‘java’、‘python’、‘数据科学’、‘算法工程师’所对应的数据，画出不同岗位对工作经验要求分布柱状图
p6obj2 = Bar()
p6obj2.add_xaxis(yindex)
p6obj2.add_yaxis("java", list(data_gr1['java'].reindex(yindex)), gap="0%")
p6obj2.add_yaxis("python", list(data_gr1['python'].reindex(yindex)), gap="0%")
p6obj2.add_yaxis("数据科学", list(data_gr1['数据科学'].reindex(yindex)), gap="0%")
p6obj2.add_yaxis("算法工程师", list(data_gr1['算法工程师'].reindex(yindex)), gap="0%")
p6obj2.set_global_opts(title_opts=opts.TitleOpts(title="不同岗位对经验要求分布柱状图"))

# 当这个程序有可能被导入时，写这个判断
# 直接用python程序调用当前这个脚本时，__name__为__main__，执行下面
# 当这个程序被导入时，__name__不为__main__，便不会执行
if __name__ == '__main__':
    page = Page(layout=Page.SimplePageLayout)
    page.add(p6obj1,p6obj2)
    TT = page.render("6.不同岗位对学历和工作经验要求分布柱状图.html")