# 将其他文件导入
import p1,p2,p3,p4,p5,p6


'''
此时p1,p2,p3,p4,p5,p6文件中的if __name__ == '__main__':语句就发挥了作用
此时为被导入的情况，p1,p2,p3,p4,p5,p6中的__name__ 就不为 '__main__'，便不会在原来的文件中再生成页面
'''

from pyecharts.charts import Tab
# 选项卡页面
tab = Tab()
# 把每一个做成一个选项卡，放入其中
tab.add(p1.p1obj,'各岗位占比饼图')
tab.add(p2.p2obj,'各岗位平均起薪柱状图')
tab.add(p3.p3obj.overlap(p3.line),'各城市招聘量柱状图及平均薪资折线图组合')
tab.add(p4.p4obj,'各城市岗位薪资分布热力图')
tab.add(p5.p5obj2,'数据科学岗位技能要求词云')
tab.add(p5.p5obj1,'数据科学工具要求排行柱状图')
tab.add(p6.p6obj1,'不同岗位对学历要求分布柱状图')
tab.add(p6.p6obj2,'不同岗位对工作经验要求分布柱状图')

# 生成页面
tab.render("combine.html")

