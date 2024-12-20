import random
from colorama import Fore, Style
import requests
import os
import times
import argparse
import textwrap
from urllib3.exceptions import InsecureRequestWarning

current_dir = os.path.dirname(os.path.abspath(__file__))
url_file = os.path.join(current_dir, "urls.txt")
path_file = os.path.join(current_dir, "paths.txt")
end_file = os.path.join(current_dir,"200.txt")
result_file = os.path.join(current_dir,"end.txt")
concat_file = os.path.join(current_dir,"concat.txt")
keyword_file = os.path.join(current_dir,'keword_url.txt')



banner = """

  ____  ______  _  __   ____  ______  _  __
_/ ___\/  _ \ \/ \/ / _/ ___\/  _ \ \/ \/ /
\  \__(  <_> )     /  \  \__(  <_> )     / 
 \___  >____/ \/\_/    \___  >____/ \/\_/  
     \/                    \/              
"""
print(banner)

user_agents = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.8.661 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.7.24 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.7.476 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0; rv:83.8.181) Gecko/20100101 Firefox/83.8.181',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.135 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.7.366 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.5.698 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.3.460 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.1.372) Gecko/20100101 Firefox/108.1.372',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.6.932 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.6.828) Gecko/20100101 Firefox/54.6.828',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.3.436 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.8.513) Gecko/20100101 Firefox/57.8.513',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.1.905 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.4.208 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.4.458 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.7.42 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.2.482 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.368 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.5.949 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0.348) Gecko/20100101 Firefox/65.0.348',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_7; rv:59.9.123) Gecko/20100101 Firefox/59.9.123',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.7.577 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_2; rv:68.4.629) Gecko/20100101 Firefox/68.4.629',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2; rv:91.8.288) Gecko/20100101 Firefox/91.8.288',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.7.579 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.4.136 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.4.54 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5; rv:106.1.365) Gecko/20100101 Firefox/106.1.365',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.4.710 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.1.438) Gecko/20100101 Firefox/87.1.438',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.7.986 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.7.988 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5; rv:52.1.396) Gecko/20100101 Firefox/52.1.396',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.2.950 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.6.384 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.1.210 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3; rv:104.7.873) Gecko/20100101 Firefox/104.7.873',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7; rv:76.3.698) Gecko/20100101 Firefox/76.3.698',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.6.510 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.4.328 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.3.742) Gecko/20100101 Firefox/61.3.742',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.6.402) Gecko/20100101 Firefox/76.6.402',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.3.182 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.36 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.5.887 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:116.5.701) Gecko/20100101 Firefox/116.5.701',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.4.316 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.9.612 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.4.180 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.6.932 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.6.466 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.6.577) Gecko/20100101 Firefox/86.6.577',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0.399) Gecko/20100101 Firefox/78.0.399',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.41 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.6.776 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.6.389) Gecko/20100101 Firefox/97.6.389',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.1.914 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.3.408 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.9.462 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.1.229) Gecko/20100101 Firefox/77.1.229',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0; rv:76.7.390) Gecko/20100101 Firefox/76.7.390',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.9.946 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.8.337 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.7.679 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2; rv:51.4.684) Gecko/20100101 Firefox/51.4.684',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.6.695 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.1.931 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.4.959) Gecko/20100101 Firefox/85.4.959',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.1.672 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.1.649) Gecko/20100101 Firefox/88.1.649',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.6.616 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4; rv:100.2.821) Gecko/20100101 Firefox/100.2.821',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.5.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.3.592) Gecko/20100101 Firefox/120.3.592',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.4.549 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.8.357 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.6.495) Gecko/20100101 Firefox/98.6.495',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6; rv:61.7.330) Gecko/20100101 Firefox/61.7.330',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.3.820 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.3.988 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6; rv:70.6.375) Gecko/20100101 Firefox/70.6.375',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
]

x_forwarded_fors = {
    '10.200.9.118',
    '10.214.244.54',
    '10.91.109.173',
    '172.29.82.24',
    '192.168.43.139',
    '172.25.113.233',
    '192.168.9.80',
    '10.50.162.124',
    '10.247.195.197',
    '172.27.46.69',
    '10.102.251.113',
    '172.26.87.212',
    '192.168.61.112',
    '10.144.227.3',
    '192.168.20.244',
    '172.17.11.20',
    '10.13.19.14',
    '10.206.22.215',
    '10.146.151.41',
    '10.214.209.195',
    '192.168.101.160',
    '10.53.34.253',
    '172.31.48.130',
    '172.16.73.159',
    '192.168.54.155',
    '192.168.83.207',
    '192.168.137.100',
    '172.23.157.157',
    '10.207.86.76',
    '172.23.92.95',
    '10.17.156.13',
    '192.168.229.142',
    '10.223.31.181',
    '10.101.162.249',
    '10.47.17.222',
    '172.17.153.140',
    '10.58.39.14',
    '172.31.147.96',
    '172.27.51.73',
    '10.234.199.139',
    '10.199.8.176',
    '192.168.4.168',
    '192.168.115.143',
    '192.168.155.109',
    '172.20.218.123',
    '172.29.86.190',
    '10.68.133.4',
    '10.226.103.210',
    '192.168.9.213',
    '192.168.168.176',
    '127.0.0.1',
    'localhost'
}

keywords = {
    r'[^0-9]((\d{8}(0\d|10|11|12)([0-2]\d|30|31)\d{3}$)|(\d{6}(18|19|20)\d{2}(0[1-9]|10|11|12)([0-2]\d|30|31)\d{3}(\d|X|x)))[^0-9]',
    r'[^\w]((?:(?:\+|00)86)?1(?:(?:3[\d])|(?:4[5-79])|(?:5[0-35-9])|(?:6[5-7])|(?:7[0-8])|(?:8[\d])|(?:9[189]))\d{8})[^\w]',
    r'[^0-9]((127\.0\.0\.1)|(10\.\d{1,3}\.\d{1,3}\.\d{1,3})|(172\.((1[6-9])|(2\d)|(3[01]))\.\d{1,3}\.\d{1,3})|(192\.168\.\d{1,3}\.\d{1,3}))',
    r'(^([a-fA-F0-9]{2}(:[a-fA-F0-9]{2}){5})|[^a-zA-Z0-9]([a-fA-F0-9]{2}(:[a-fA-F0-9]{2}){5}))',
    r'(((access)(|-|_)(key)(|-|_)(id|secret))|(LTAI[a-z0-9]{12,20}))',
    r'((\'|")(|[\w]{1,10})([p](ass|wd|asswd|assword))(|[\w]{1,10})(\'|")(:|=)( |)\'|"(.*?)\'|")(|,))'
    r'((\'|")(|[\w]{1,10})(([u](ser|name|sername))|(account)|((((create|update)((d|r)|(by|on|at)))|(creator))))(|[\w]{1,10})(\'|")(:|=)( |)\'|"(.*?)\'|")(|,))'
    r'((corp)(id|secret))',
    r'(\$router\.push)',
    r'((access=)|(adm=)|(admin=)|(alter=)|(cfg=)|(clone=)|(config=)|(create=)|(dbg=)|(debug=)|(delete=)|(disable=)|(edit=)|(enable=)|(exec=)|(execute=)|(grant=)|(load=)|(make=)|(modify=)|(rename=)|(reset=)|(root=)|(shell=)|(test=)|(toggl=))',
    r'(=deleteMe|rememberMe=)',
    r'((swagger-ui.html)|(\"swagger\":)|(Swagger UI)|(swaggerUi)|(swaggerVersion))',
    r'(eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9._-]{10,}|eyJ[A-Za-z0-9_\/+-]{10,}\.[A-Za-z0-9._\/+-]{10,})',
    r'(Druid Stat Index)',
    r'(ueditor\.(config|all)\.js)',
    r'(([a-z0-9]+[_|\.])*[a-z0-9]+@([a-z0-9]+[-|_|\.])*[a-z0-9]+\.((?!js|css|jpg|jpeg|png|ico)[a-z]{2,5}))'
    r"(?:username|user|account|email)\s*[:=]\s*([^\s]+)",
    r"(?:password|passwd|pwd|secret)\s*[:=]\s*([^\s]+)",
    r"(?:[\u4e00-\u9fa5]+省)?(?:[\u4e00-\u9fa5]+市)(?:[\u4e00-\u9fa5]+区)?(?:[\u4e00-\u9fa5]+街道)?(?:[\u4e00-\u9fa5]+路)?(?:[\u4e00-\u9fa5A-Za-z0-9\-]*号)?(?:[\u4e00-\u9fa5A-Za-z0-9\-]*室)?"
}


with open(url_file, "r", encoding="utf-8") as f:
    urls = f.readlines()
with open(path_file, "r", encoding="utf-8") as f:
    paths = f.readlines()




with open(concat_file,"w",encoding="utf-8") as f:
    for url in urls:
        for path in paths:
            full_url = url.strip() + path.strip()
            f.write(full_url + '\n')




## 工具作用主题函数
def request_url(concat_url):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    try:
        # 第一次请求：不带 X-Forwarded-For 头
        headers = {
            'User-Agent': random.choice(user_agents)
        }
        response1 = requests.get(concat_url, headers=headers, verify=False)
        response2 = requests.post(concat_url, headers=headers, data={}, verify=False)

        if response1.status_code == 200 or response2.status_code == 200:
            # 保存 200 状态的 URL

            with open(end_file, "a", encoding="utf-8") as f:
                f.write(f"URL: {concat_url} + STATUS-CODE: {response1.status_code} '\n'")
            print(f"发现存活 URL：{concat_url}  状态码: {response1.status_code}" + Style.RESET_ALL)

                ## 匹配关键词
            content1 = response1.text
            content2 = response2.text
            match_keywords = [keyword for keyword in keywords if keyword in content1 or keyword in content2]
            with open(keyword_file, 'a', encoding='utf-8') as f:
                f.write(f"URL: {concat_url} 匹配到的关键词: {', '.join(match_keywords)}\n")
            print(Fore.GREEN + f"[匹配成功] {concat_url} 匹配到关键词: {', '.join(match_keywords)}" + Style.RESET_ALL)



        elif response1.status_code == 403 or response2.status_code == 403:
            # 第二次请求：逐一尝试 X-Forwarded-For 头
            for xff in x_forwarded_fors:
                headers['X-Forwarded-For'] = xff
                response1 = requests.get(concat_url, headers=headers, verify=False)
                response2 = requests.post(concat_url, headers=headers, data={}, verify=False)
                if response1.status_code == 200 or response2.status_code == 200:
                    # 如果尝试后状态变为 200，则保存

                    print(Fore.GREEN +f"【403变200】发现存活 URL：{concat_url}  状态码: {response1.status_code}  XFF: {xff}" + Style.RESET_ALL)
                    with open(end_file, "a", encoding="utf-8") as f:
                        f.write(f"URL: {concat_url} + XFF: {xff} + STATUS-CODE: '\n'")

                    content1 = response1.text
                    content2 = response2.text
                    match_keywords = [keyword for keyword in keywords if keyword in content1 or keyword in content2]
                    with open(keyword_file, 'a', encoding='utf-8') as f:
                        f.write(f"URL: {concat_url} 匹配到的关键词: {', '.join(match_keywords)}\n")
                    print(Fore.GREEN + f"[匹配成功] {concat_url} 匹配到关键词: {', '.join(match_keywords)}")
                    ## 匹配关键词
                    break  # 成功后退出 X-Forwarded-For 尝试循环
                else:
                    print(f"尝试 XFF {xff} 未成功：{concat_url}  状态码: {response1.status_code}")
            else:
                # 如果所有 XFF 都尝试后仍然 403，记录日志
                print(f"所有 XFF 尝试后仍然 403：{concat_url}")

        else:
            print(f"未发现存活：{concat_url}  状态码: {response1.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"网络连接错误：{e} 请退出重新运行")

# 读取文件中的 URL 并进行请求
 # 拼接后的 URL 文件
with open(concat_file, "r", encoding="utf-8") as f:
    concat_urls = f.readlines()
    for concat_url in concat_urls:
        request_url(concat_url.strip())


