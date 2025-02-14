import pandas as pd  
from pyecharts.charts import Line  
from pyecharts import options as opts  
from datetime import datetime  

# 读取 Excel 文件  
df = pd.read_excel(r'C:\Users\61985\Desktop\Chiang Mai_2024.xlsx')  

# 检查列名  
print("列名：", df.columns)  

# 数据预处理  
df['Datetime (CST)'] = pd.to_datetime(df['Datetime (CST)'])  # 转换时间列为 datetime 类型  
df['temp'] = df['temp'].astype(float)  # 确保温度为浮点数  
df['rhum'] = df['rhum'].astype(float)  # 确保湿度为浮点数  

# 按季度划分数据  
def filter_by_quarter(data, start_date, end_date):  
    return data[(data['Datetime (CST)'] >= start_date) & (data['Datetime (CST)'] < end_date)]  

# 绘制温湿度曲线  
def draw_line_chart(data, title, output_file):  
    x_data = data['Datetime (CST)'].dt.strftime('%Y-%m-%d %H:%M').tolist()  
    y_temp = data['temp'].tolist()  
    y_humidity = data['rhum'].tolist()  
    
    line = (  
        Line()  
        .add_xaxis(x_data)  
        .add_yaxis(  
            "温度 (°C)",  
            y_temp,  
            is_smooth=True,  
            is_symbol_show=False,  
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_='max', name='最高温度')]),  
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color="rgba(255, 0, 0, 0.5)"),  
            itemstyle_opts=opts.ItemStyleOpts(color="rgba(255, 0, 0, 0.8)")  
        )  
        .add_yaxis(  
            "湿度 (%)",  
            y_humidity,  
            is_smooth=True,  
            is_symbol_show=False,  
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_='max', name='最高湿度')]),  
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color="rgba(0, 0, 255, 0.5)"),  
            itemstyle_opts=opts.ItemStyleOpts(color="rgba(0, 0, 255, 0.8)")  
        )  
        .set_global_opts(  
            title_opts=opts.TitleOpts(title=title, pos_left="8%", pos_top="top"),  # 修改标题位置为左上方  
            tooltip_opts=opts.TooltipOpts(trigger="axis"),  
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)),  
            yaxis_opts=opts.AxisOpts(name="温度 (°C)", min_=-10, max_=100),  
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]  
        )  
    )  
    line.render(output_file)  

# 绘制每个季度的温湿度曲线  
quarters = [  
    ("2024-01-01", "2024-04-01", "Chiang Mai_2024_Q1温湿度曲线", "2024Q1_T&RH.html"),  
    ("2024-04-01", "2024-07-01", "Chiang Mai_2024_Q2温湿度曲线", "2024Q2_T&RH.html"),  
    ("2024-07-01", "2024-10-01", "Chiang Mai_2024_Q3温湿度曲线", "2024Q3_T&RH.html"),  
    ("2024-10-01", "2025-01-01", "Chiang Mai_2024_Q4温湿度曲线", "2024Q4_T&RH.html"),  
]  

for start, end, title, output in quarters:  
    quarter_data = filter_by_quarter(df, start, end)  
    draw_line_chart(quarter_data, title, output)  

# 绘制全年温湿度曲线  
draw_line_chart(df, "Chiang Mai_2024温湿度曲线", "2024_T&RH.html")
