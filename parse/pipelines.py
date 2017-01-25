# -*- coding: utf-8 -*-

import json

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('sport.json', 'wb')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class ParsePipeline(object):
    def process_item(self, item, spider):
        return item
