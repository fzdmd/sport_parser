# -*- coding: utf-8 -*-

import json
import re

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('sport.json', 'wb')

    def close_spider(self, spider): 
        self.file.close()

    def process_item(self, item, spider):
        for k,v in item.items():
           item[k] = re.sub('\s+', ' ', v).strip();
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

