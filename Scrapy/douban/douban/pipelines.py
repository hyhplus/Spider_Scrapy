# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from douban.settings import mongo_db_collect, mongo_db_name, mongo_host,mongo_port


class DoubanPipeline(object):
    # 数据加工,保存到数据库

    def __init__(self):
        host = mongo_host
        port = mongo_port
        db = mongo_db_name
        table = mongo_db_collect

        client = pymongo.MongoClient(host=host, port=port)

        myDB = client[db]
        self.post = myDB[table]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
