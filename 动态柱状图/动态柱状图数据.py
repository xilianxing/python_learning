from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
# 为timeline设置主题需要导入的包
f = open("D:/1960-2019全球GDP数据.csv","r",encoding="GB2312")
# .csv文件通过记事本打开后采用的是ANSI编码，所以不使用utf-8的万国码
# 而是用GB2312的简体中文编码
f_data = f.readlines()
# 按行读取，每行作为一个元素，存在一个列表中，包裹\n换行符
f.close()
# f_data.replace("year,GDP,rate\n","")列表没有replace方法，字符串有
# f_data.pop(0)
f_data.remove("year,GDP,rate\n")
# print(f_data)
# 删除第一行数据
# 将数据转化为字典格式：
# {年份:[[country,GDP],[country,GDP],[country,GDP]....],年份:[[country,GDP],[country,GDP],[country,GDP]....],年份:[[country,GDP],[country,GDP],[country,GDP]....],....}
data_dict = {}
# 先定义一个空dict
for line in f_data:
    years = int(line.split(",")[0])
    country = line.split(",")[1]
    GDP = float(line.split(",")[2])
    # .csv文件在记事本中打开后，每行数据中通过“，”隔开
    try:
        data_dict[years].append([country,GDP])
    except KeyError:
        data_dict[years] = []
        data_dict[years].append([country,GDP])
        # 这里的异常捕获是通过第一次except捕获字典中没有key值
        # 并添加第一个年份作为key值以及一个空列表作为对应值
        # 即：{years:[]},然后再通过append方法追加key值对应的列表
sorted_data = sorted(data_dict)
# print(sorted_data)
timeline = Timeline(init_opts=InitOpts(width="1300px",height="700px",theme=ThemeType.LIGHT))
# 设置一个主题
for years in sorted_data:
    data_dict[years].sort(key = lambda element:element[1],reverse = True)
    # 列表的sort方法搭配lambda匿名函数对嵌套列表中的各列表进行排序
    # reverse为Flase，数据从小到大排序
    data_dict_list = data_dict[years][0:8]
    # 取前8名，用序列的切片操作
    x_data = []
    y_data = []
    for country_gdp in data_dict_list:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1]/100000000)
        # 数据数量级过大的处理
    x_data.reverse()
    y_data.reverse()
    # 调转x，y轴数据，修改较大的数据位于最下侧的问题
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)",y_data,label_opts=LabelOpts(is_show= True,position="right"))
    # 将柱状图数据放在柱状图右侧
    bar.reversal_axis()
    # 反转x,y轴
    bar.set_global_opts(
        title_opts=TitleOpts(title = f"{years}年全球gdp前8名",pos_left="left"),
        legend_opts = LegendOpts(is_show=True, pos_left="right", orient="vertical", pos_bottom='50%'),
        # 图例选项：图例位置pos_left,pos_right(图例与左右间距的距离),pos_bottom(图例与底部的距离，单位：%)
        # 图例纵向分布：orient="vertical"
        toolbox_opts = ToolboxOpts(is_show=True),
        visualmap_opts = VisualMapOpts(is_show=True, min_=1, max_=8, pos_right="right"),
        # datazoom_opts = DataZoomOpts(is_show=True)
        # 数据缩放
    )
    # 添加一个标题
    timeline.add(bar,str(years))
    # 每一次循环将绘制的柱状图和年份（年份作为时间点）传入时间线
    timeline.add_schema(
        # 传入时间线的参数，关键字传参
        play_interval=300,
        # 单位是毫秒
        is_timeline_show=True,
        # 是否显示时间轴
        is_auto_play=True,  # 自动播放
        is_loop_play=True,  # 循环播放
    )
timeline.render ("动态柱状GDP数据.html")






