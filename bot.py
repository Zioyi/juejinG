import requests
import time
import random

url = "https://api.juejin.cn/content_api/v1/article/detail"
data = {
    "article_id": "694547078999149"
}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

cnt = 0
msg = [
    "<%d,%d>########[%d]",
    "####<%d,%d>####[%d]",
    "########<%d,%d>[%d]",
]

total = random.randint(30, 50)
for _ in range(total):
    res = requests.post(url, json=data, headers=headers)
    # print(res.status_code, res.json())
    assert res.status_code == 200
    block = random.randint(1, 3)
    time.sleep(block)
    cnt += 1
    print(msg[cnt % 3] % (cnt % 10, block, cnt), end="\r")
