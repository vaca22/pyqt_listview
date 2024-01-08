import requests

# Define the URL and the headers
url = 'https://channels.weixin.qq.com/shop-faas/mmchannelstradehome/api/home'
headers = {
    'Connection': 'keep-alive',
    'xweb_xhr': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819) XWEB/8531',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

# Define the cookies
cookies = {
    'biz_token': 'b_0000018c_e4075dcb_6104ed4b_4a44049e_2c98777d',
    'biz_ticket': 'giecnEOjBVCSdPyhgWKDsGLrAAAAAAAAAAAAAAAAAAA=',
    'biz_expire': '1704690337',
    'biz_rand': 'CAESILoq6d4GPYz9FeExynatNjL3exRcMlDK2XlXNpUHZ10K',
    'faas_logId': '8b0a8f86-0ce6-4815-8ec2-7c2eeb40a1d3',
    'faas_logPageId': '11a50e43-b258-4ad3-8b49-3465246a410f',
    'faas_logOperationId': '17'
}

# Make the GET request
response = requests.get(url, headers=headers, cookies=cookies)

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful.")
    print(response.text)
    # Process the response if needed
    # data = response.json()
else:
    print(f"Request failed with status code: {response.status_code}")