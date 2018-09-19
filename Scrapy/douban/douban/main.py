from scrapy import cmdline

# 直接执行main.py即可执行整个`douban`爬虫程序
cmdline.execute('scrapy crawl douban_spider'.split())
