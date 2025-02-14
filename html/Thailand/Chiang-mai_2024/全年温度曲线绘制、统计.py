import os  
import pandas as pd  
from pyecharts.charts import Line  
from pyecharts import options as opts  
from pyecharts.globals import ThemeType  

def generate_temperature_chart(df):  
    # 数据预处理  
    df['Datetime (CST)'] = pd.to_datetime(df['Datetime (CST)'])  
    df['Temp'] = df['temp']  # 使用温度列  

    # 统计超过30℃、35℃、40℃的总时间  
    temp_30 = df[df['Temp'] >= 30].shape[0]  
    temp_35 = df[df['Temp'] >= 35].shape[0]  
    temp_40 = df[df['Temp'] >= 40].shape[0]  

    # 计算每日最高和最低温度  
    daily_temps = df.groupby(df['Datetime (CST)'].dt.date)['Temp'].agg(['max', 'min']).reset_index()  

    # 确保日期列是 datetime 类型  
    daily_temps['Datetime (CST)'] = pd.to_datetime(daily_temps['Datetime (CST)'])  

    # 准备 x 轴和 y 轴数据  
    x_data = daily_temps['Datetime (CST)'].dt.strftime('%Y-%m-%d').tolist()  
    y_data_max = daily_temps['max'].tolist()  
    y_data_min = daily_temps['min'].tolist()  

    # 获取全年最高温度  
    max_temp = max(y_data_max)  

    # 绘制折线图  
    line = (  
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # 使用浅色主题  
        .add_xaxis(x_data)  
        .add_yaxis(  
            "最高气温", y_data_max,  
            color="red",  # 设置最高气温曲线为红色  
            areastyle_opts=opts.AreaStyleOpts(  
                opacity=0.5,  
                color={  
                    "type": "linear",  # 渐变类型  
                    "x": 0, "y": 0, "x2": 0, "y2": 1,  # 渐变方向：从上到下  
                    "colorStops": [  
                        {"offset": 0, "color": "red"},  # 起始颜色：红色（最高气温）  
                        {"offset": 1, "color": "blue"}  # 结束颜色：蓝色（最低气温）  
                    ]  
                }  
            ),  
            is_symbol_show=False,  
            markline_opts=opts.MarkLineOpts(data=[  
                opts.MarkLineItem(type_='value', y=30, name=f'30°C线，{temp_30}小时'),  
                opts.MarkLineItem(type_='value', y=35, name=f'35°C线，{temp_35}小时'),  
                opts.MarkLineItem(type_='value', y=40, name=f'40°C线，{temp_40}小时'),  
                opts.MarkLineItem(  
                    type_='value',   
                    y=max_temp,   
                    name=f'最高温度线：{max_temp}°C',  
                    linestyle_opts=opts.LineStyleOpts(color="red", width=2, type_="dashed")  # 设置红色虚线  
                ),  
            ]),  
            markpoint_opts=opts.MarkPointOpts(data=[  
                opts.MarkPointItem(coord=[0, 30], value=f'{temp_30}小时', name='30°C统计'),  
                opts.MarkPointItem(coord=[0, 35], value=f'{temp_35}小时', name='35°C统计'),  
                opts.MarkPointItem(coord=[0, 40], value=f'{temp_40}小时', name='40°C统计'),  
            ])  
        )  
        .add_yaxis(  
            "最低气温", y_data_min,  
            color="blue",  # 设置最低气温曲线为蓝色  
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),  
            is_symbol_show=False,  
        )  
        .set_global_opts(  
            title_opts=opts.TitleOpts(  
                title=f"Chiang Mai_2024年气温分布\n≥30°C：{temp_30}H，≥35°C：{temp_35}H，≥40°C：{temp_40}H\nMax：{max_temp}°C",  
                pos_top="2%",  
                pos_left="10%",  
                title_textstyle_opts=opts.TextStyleOpts(color='#228be6', font_size=20)  
            ),  
            xaxis_opts=opts.AxisOpts(  
                type_="category",  
                axislabel_opts=opts.LabelOpts(rotate=-30),  
                axisline_opts=opts.AxisLineOpts(is_show=True)  
            ),  
            yaxis_opts=opts.AxisOpts(  
                axisline_opts=opts.AxisLineOpts(is_show=True)  
            ),  
            tooltip_opts=opts.TooltipOpts(trigger='axis'),  
        )  
    )  
    return line  

# 主函数  
if __name__ == '__main__':  
    file_path = r'C:\Users\61985\Desktop\Chiang Mai_2024.xlsx'  
    if not os.path.exists(file_path):  
        print(f"文件不存在：{file_path}")  
    else:  
        df = pd.read_excel(file_path)  
        chart = generate_temperature_chart(df)  
        chart.render("2024_temperature.html")
