import requests
from bs4 import BeautifulSoup
import json
import re

# 三人微博ID主页
weibo_users = {
    "张婧仪": "https://weibo.com/u/6444428225",
    "周也": "https://weibo.com/u/6421419705",
    "孙怡": "https://weibo.com/u/1642505204"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://weibo.com/"
}

def get_fans(link):
    try:
        res = requests.get(link, headers=HEADERS, timeout=15)
        res.encoding = "utf-8"
        # 正则抓粉丝数字
        match = re.search(r'粉丝[:：]\s*([\d.]+[万千]?)', res.text)
        if match:
            return match.group(1)
        return "暂无数据"
    except Exception as e:
        print("抓取异常:", e)
        return "抓取失败"

def main():
    data_list = []
    for name, url in weibo_users.items():
        fans = get_fans(url)
        data_list.append({
            "name": name,
            "fans": fans
        })
    # 写入json
    with open("fans_data.json", "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=2)
    print("✅ 数据已生成 fans_data.json")

if __name__ == "__main__":
    main()
