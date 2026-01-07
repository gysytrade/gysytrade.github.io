
import requests
import re
import json
import math

def bd09_to_gcj02(bd_lon, bd_lat):
    x_pi = 3.14159265358979324 * 3000.0 / 180.0
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gg_lon = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return gg_lon, gg_lat

def get_coordinates():
    url = "https://map.baidu.com/poi/%E4%B8%87%E8%BE%BE%E4%B8%AD%E5%BF%83/@11787255.132372316,3796887.3754877998,19z?uid=8712f1bd1648cf46fb221358&ugc_type=3&ugc_ver=1&device_ratio=1&compat=1&en_uid=8712f1bd1648cf46fb221358&pcevaname=pc4.1&querytype=detailConInfo&da_src=shareurl"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            content = response.text
            # 尝试寻找经纬度信息
            # 百度地图页面通常包含 "point":{"x":...,"y":...} 这样的结构，但这里可能是墨卡托坐标
            # 我们先打印一部分内容看看
            
            # 尝试匹配 "content":{...} 或者 "current_city":{...} 等信息
            # 也可以尝试直接匹配经纬度格式，虽然可能不存在
            
            print("Page content length:", len(content))
            
            # 搜索 "point" 关键字
            match = re.search(r'"point":\s*\{\"x\":(\d+\.\d+),\"y\":(\d+\.\d+)\}', content)
            if match:
                x = float(match.group(1))
                y = float(match.group(2))
                print(f"Found Point (likely Mercator): x={x}, y={y}")
                # 这里得到的很可能是墨卡托坐标
            else:
                print("Point not found in HTML")
                
            # 如果是墨卡托坐标，我们无法直接用简单的公式转经纬度（百度算法未公开）
            # 但是，我们可以尝试请求百度的一个公开接口（如果存在）
            # 或者，我们可以尝试搜索 "content" JSON 数据中的其他字段
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_coordinates()
