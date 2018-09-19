# -*- coding: utf-8 -*-
import scrapy
import time

from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    """
    豆瓣top250-爬虫文件
    """
    # 这里是爬虫名
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口url, 交给调度器
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        """
        默认的解析方法
        """
        # print(response.text)
        # 使用xpath规则定位到电影列表, 一页25条数据
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")

        # 循环遍历一个页面, 得到items相关所需的数据字段
        for i_item in movie_list:
            # print(item)
            # items文件的导入, 实例化DoubanTtem对象
            douban_item = DoubanItem()

            # 写详细的xpath, 进行数据解析
            douban_item['serial_number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = i_item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            # 数据处理
            first_getInfo = i_item.xpath(".//div[@class='bd']//p[1]/text()").extract()
            list_str = []
            for i_content in first_getInfo:
                content_s =  "".join(i_content.split())
                list_str.append(content_s)
                douban_item['introduce'] = content_s
                # douban_item['introduce'] = list_str[1:]

            douban_item['star'] = i_item.xpath(".//div[@class='star']//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            douban_item['describe'] = i_item.xpath(".//p[@class='quote']//span[1]/text()").extract_first()

            # 需要将数据yield到pipelines里面去
            yield douban_item

        # 解析下一页规则, 找到下一页的xpath
        next_page = response.xpath("//span[@class='next']//link/@href").extract_first()
        # print(next_page)

        if next_page:
            # next_page = next_page[0]
            next_urls = 'https://movie.douban.com/top250'+next_page
            time.sleep(2)
            # 请求下一页, 回调执行下一页的数据解析
            yield scrapy.Request(next_urls, callback=self.parse)















