import os  
import pandas as pd  
from meteostat import Point, Hourly  
from datetime import datetime  
import pytz  # 用于时区处理  
import warnings  

# 抑制FutureWarning  
warnings.filterwarnings("ignore", category=FutureWarning)  

# Chiang Mai 地区的经纬度坐标  
latitude = 18.7833  # Latitude  
longitude = 98.9833  # Longitude   

# 创建Point对象  
location = Point(latitude, longitude)  

# 设置日期范围（2024年1月1日至2024年1月11日）  
start_date = datetime(2024, 1, 1)  
end_date = datetime(2025, 1, 1)  # 结束日期为1月12日，以获取到1月11日的数据  

# 获取每小时的天气数据  
data = Hourly(location, start_date, end_date)  

# 下载数据  
weather_data = data.fetch()  

# 检查数据是否为空  
if weather_data.empty:  
    print("没有找到相关的天气数据。")  
else:  
    # 将 UTC 时间转换为 CST（UTC+8）  Asia/Singapore
    weather_data.index = weather_data.index.tz_localize('UTC').tz_convert('Asia/Bangkok')  

    # 将时间索引转换为无时区的格式  
    weather_data.index = weather_data.index.tz_localize(None)  

    # 重新设置索引名称为更有意义的格式  
    weather_data.index.name = 'Datetime (CST)'  

    # 获取桌面路径  
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")  

    # 保存为Excel文件到桌面  
    file_path = os.path.join(desktop_path, 'Chiang Mai_2024.xlsx')  

    # 使用pandas的to_excel方法保存数据  
    weather_data.to_excel(file_path, engine='openpyxl')  

    print(f"Weather data saved to {file_path}")
