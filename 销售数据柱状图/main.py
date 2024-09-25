from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.options import TitleOpts, LabelOpts, LegendOpts, ToolboxOpts, VisualMapOpts, DataZoomOpts, LabelOpts, \
    InitOpts

from data_reader import Filereader,Textfileread,Jsonfileread
from data_define import Record

textfile_data = Textfileread("D:/2011年1月销售数据.txt")
jsonfile_data = Jsonfileread("D:/2011年2月销售数据JSON.txt")

jan_data:list[Record] = textfile_data.read_file()
feb_data:list[Record] = jsonfile_data.read_file()

all_data:list[Record] = jan_data + feb_data
data_dict = {}
for record in all_data:
    # 直接调用list中每个record类对象
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money
# print(data_dict)
x_data = []
y_data = []
for date in data_dict.keys():
    x_data.append(date)
    y_data.append(data_dict[date])

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT,width="1300px",height="700px"))
# 对最终生成图像（调用render方法）的类对象进行InitOpts类对象的关键字传参
# InitOpts类对象关键字传参中可以设置主题，调整图像尺寸（数据可视化全屏最佳尺寸：width="1300px",height="700px"）
# 图像尺寸的宽高比最好是3：2
bar.add_xaxis(x_data)
bar.add_yaxis("销售额",y_data,label_opts=LabelOpts(is_show = False))
# bar.add_xaxis(list(data_dict.keys()))
# bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show = False))
# 比较简单的代码写法
bar.set_global_opts(
    title_opts=TitleOpts(title = "1~2月每日销售额柱状统计图",pos_left="center",pos_bottom='0%'),
    legend_opts=LegendOpts(is_show=True,pos_left="right",orient="vertical",pos_bottom='50%'),
    # 图例选项：图例位置pos_left,pos_right(图例与左右间距的距离),pos_bottom(图例与底部的距离，单位：%)
    # 图例纵向分布：orient="vertical"
    toolbox_opts=ToolboxOpts(is_show=True),
    # 工具箱选项
    visualmap_opts= VisualMapOpts(is_show=True,min_=50000,max_=110000,pos_right="right"),
    # 可视化选项控制着数值—颜色的变化，对相应数据分析，定义合适的最大值最小值
    datazoom_opts= DataZoomOpts(is_show=True)
)
bar.render("1~2月每日销售额统计柱状图.html")









