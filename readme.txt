使用方法：

目录下创建urls.txt和paths.txt
urls.txt作用： 填入http://xxxx/等url，一行一个
paths.txt作用： 填入xxx/xx/等路径，一行一个
200.txt会保存存活的完整url和匹配到关键字的url
concat.txt会保存拼接好的完整url

注意： 填入url和path的时候不要留空格
此工具我使用了随机UA头防爬虫封禁，同时增加了XFF头绕403状态的url，还增加了正则匹配敏感内容，如：shiro、身份证等
目前工具只能简单扫描，后续更新会逐渐完善自动绕403的方式、敏感匹配的正则库、防封禁方式等


命令行采用傻瓜式运行：
python cowcow.py
