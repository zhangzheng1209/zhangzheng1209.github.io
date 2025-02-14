import os  
import pandas as pd  
import plotly.express as px  

# 获取桌面路径  
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")  

# 设置文件路径  
file_path = os.path.join(desktop_path, 'Chiang Mai_2024.xlsx')  # 确保文件名正确  

# 检查文件是否存在  
if not os.path.exists(file_path):  
    print(f"文件 {file_path} 不存在，请检查路径和文件名。")  
else:  
    # 读取 Excel 文件  
    weather_data = pd.read_excel(file_path, index_col='Datetime (CST)')  

    # 筛选温度 ≥30°C 且湿度 ≥60% 的数据  
    filtered_data = weather_data[(weather_data['temp'] >= 30) & (weather_data['rhum'] >= 60)]  

    # 按日期统计满足条件的小时数  
    daily_stats = filtered_data.resample('D').size().reset_index(name='Hour Count')  

    # 统计总的小时数  
    total_hours = daily_stats['Hour Count'].sum()  

    # 绘制图形  
    fig = px.bar(daily_stats, x='Datetime (CST)', y='Hour Count',  
                 title=f'Daily Count of Hours with Temp ≥30°C & Hum ≥60% in Chiang Mai_2024 (2024)<br>Total Hours: {total_hours}',  
                 labels={'Datetime (CST)': 'Date', 'Hour Count': 'Number of Hours'})  

    # 保存为 HTML 文件  
    html_file_path = os.path.join(desktop_path, '2024_Stats.html')  
    fig.write_html(html_file_path)  

    print(f"图形已保存为 HTML 文件: {html_file_path}")
