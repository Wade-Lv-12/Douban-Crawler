import requests
from bs4 import BeautifulSoup
import time

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    "referer": "https://movie.douban.com/"
}

for start_num in range(0, 250, 25):
    try:
        response = requests.get(f"https://movie.douban.com/top250?start={start_num}&filter=", headers=headers)
        response.raise_for_status()  # 确保响应状态是200
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        
        all_titles = soup.findAll("span", attrs={"class": "title"})
        for title in all_titles:
            title_string = title.string
            if "/" not in title_string:  # 排除中英文名称带斜杠的情况
                print(title_string)
    except requests.RequestException as e:
        print(f"请求失败: {e}")
    
    time.sleep(1)  # 每次请求后等待1秒
