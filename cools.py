# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 18:01:53 2017

@author: Administrator
"""

import scrapy
from scrapy.loader import ItemLoader
from coolspyder.items import CoolspyderItem
URL = 'http://zhidao.baidu.com'

class CoolSpider(scrapy.Spider):
    name = "cool"
    allowed_domains=['zhidao.baidu.com/question/']
    start_urls = [
        'https://zhidao.baidu.com/question/582606552.html?fr=iks&word=%B1%C7%D1%D7'
        ]
  

    def parse(self, response):
        
        #下一步要把h3改为需要的html元素来进行爬取
        '''l=ItemLoader(item=CoolspyderItem(), response=response)
        l.add_xpath('description','//meta[@name="description"]')
        l.add_xpath('answer','//div[@class="long-question"]')'''
        '''
        for h3 in response.xpath('//meta[@name="description"]').extract():
            if "鼻炎" in h3:
                f=open('test.txt','a')
                f.write(h3)
                f.write('\n')
                
                for h4 in response.xpath('//div[@class="long-question"]').extract():
                    f.write(h4)
                    f.write('\n')
                f.close()
            else :
                continue
            yield {"title": h3}
            
        '''
        for url in response.xpath('//a/@href').extract():
            if not ( url.startswith('http://') or url.startswith('https://') ):
                
                url= URL + url
                
            
            yield scrapy.Request(url=url, callback=self.parse)
