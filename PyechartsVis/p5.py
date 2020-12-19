from pyecharts.charts import Bar,WordCloud,Page
from pyecharts import options as opts

import re
import collections
import jieba

'''
5. 数据科学工具要求排行柱状图和岗位技能要求词云
'''

# 1 读取数据
# 从publicFunction中导入read_works函数和word_count函数
from publicFunction import read_works,word_count
# 调用此函数，完成数据的读取和处理
data_cy = read_works()
# 只拿出数据科学的岗位进行分析
data_cy = data_cy[data_cy['岗位类别'] == '数据科学'].copy()

# 2 拼接所有岗位描述
string_data = ''
for i in data_cy['岗位描述']:
    string_data += str(i)

# 从大字符串中取出所有英文单词
list1 = re.findall('[a-zA-Z]+', string_data, flags=re.S)
# 把所有取出的英文单词转换成大写
list2 = [item1.upper() for item1 in list1]
# print(list2)


word_counts = collections.Counter(list2)  # 对分词做词频统计
word_counts_top = word_counts.most_common(10)  # 获取前10最高频的词


# 绘出数据分析所需工具排行最高的柱状图
p5obj1 = Bar()
p5obj1.add_xaxis([i[0] for i in word_counts_top])
p5obj1.add_yaxis("数据分析工具", [i[1] for i in word_counts_top], color='#CD1076')
p5obj1.set_global_opts(
    title_opts=opts.TitleOpts(title="数据分析工具排行"),
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15))
)



# 绘制岗位要求词云图
# 调用word_count函数，进行文本处理，并提取词频排行前100的词
word_counts = word_count(string_data)

# 绘制词云
p5obj2 = WordCloud()
p5obj2.add(
        series_name="岗位技能要求", data_pair=word_counts, word_size_range=[20, 80],
    )
p5obj2.set_global_opts(
        title_opts=opts.TitleOpts(title="岗位技能要求"),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )


# 当这个程序有可能被导入时，写这个判断
# 直接用python程序调用当前这个脚本时，__name__为__main__，执行下面
# 当这个程序被导入时，__name__不为__main__，便不会执行
if __name__ == '__main__':
    page = Page()
    page.add(p5obj2,p5obj1)
    page.render('5.数据科学工具要求排行柱状图和岗位技能要求词云.html')




