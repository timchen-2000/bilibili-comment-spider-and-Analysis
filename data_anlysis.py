import requests
import re
import json


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
    }

def get_oid(video_url):
    # 发送请求获取页面内容
    resp = requests.get(video_url, headers=headers)
    if resp.status_code == 200:
        # 使用正则表达式匹配oid
        oid_pattern = re.compile(r'window.__INITIAL_STATE__=({.*?});\(', re.DOTALL)
        oid_match = oid_pattern.search(resp.text)
        if oid_match:
            data_json = oid_match.group(1)
            data = json.loads(data_json)
            oid = data['videoData']['pages'][0]['cid']
            return oid
        else:
            print("未找到oid")
            return None
    else:
        print(f"请求失败，状态码：{resp.status_code}")
        return None

# 示例视频链接
video_url = "https://www.bilibili.com/video/BV17kJ7zjECm/?vd_source=ca0600d3849225b96f47accf71e75810"

# 调用函数获取oid
oid = get_oid(video_url)
url=f"https://api.bilibili.com/x/v1/dm/list.so?oid={oid}"
res = requests.get(url=url,headers=headers)
with open('233.xml', 'wb') as f:
    f.write(res.content)



# res.encoding='utf-8'
# content_list=re.findall('<d p=".*?">(.*?)</d>',res.text)
# print(content_list)