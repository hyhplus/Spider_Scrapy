from scrapy import cmdline

# 直接执行main.py即可执行整个爬虫程序
cmdline.execute('scrapy crawl douban_spider'.split())