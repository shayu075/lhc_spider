# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from lhc_spider.spiders.utils import get_list_by_30m, get_date_by_qs, get_tuple_by_ws, get_tuple_by_bs, get_tuple_by_sx, get_tuple_by_3t
from lhc_spider.items import LhcSpiderItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        # 30m-王中王
        yield Request(url='http://www.240303.com/bbs/2422.htm', callback=self.parse_30m, dont_filter=True)
        # ws-周某人
        yield Request(url='http://www.zmr00.com/bbs/013.htm', callback=self.parse_ws, dont_filter=True)
        # bs双波-东方红
        yield Request(url='http://www.672525.com/#kj50000', callback=self.parse_bs, dont_filter=True)
        # 七肖-美猴王论坛
        # yield Request(url='http://www.801737.com/bbs/006.htm', callback=self.parse_sx, dont_filter=True)
        # 七肖
        yield Request(url='http://www.68496.com/bbs2/bbs/7肖.htm', callback=self.parse_7x, dont_filter=True)
        # 三头
        yield Request(url='http://www.68496.com/bbs2/bbs/3头.htm', callback=self.parse_3t, dont_filter=True)

    def parse_30m(self, response):
        all_tr = response.css('#table400915489 table tr')
        tmp_qs = ''
        tmp_cc = []
        for index, x in enumerate(all_tr, start=0):
            _yu = index % 6
            if _yu == 0:
                tmp_qs = x.css('::text').extract()[2].replace('第', '').replace('期', '')
            elif _yu == 1:
                pass
            elif _yu == 2:
                tmp_cc += get_list_by_30m(x.css('::text').extract())
            elif _yu == 3:
                tmp_cc += get_list_by_30m(x.css('::text').extract())
            elif _yu == 4:
                tmp_cc += get_list_by_30m(x.css('::text').extract())
            elif _yu == 5:
                if tmp_cc:
                    date = get_date_by_qs(tmp_qs)
                    if date:
                        spi_item = LhcSpiderItem()
                        spi_item['id'] = date[0]
                        spi_item['qs'] = date[1]
                        spi_item['year'] = date[2]
                        spi_item['month'] = date[3]
                        spi_item['day'] = date[4]
                        spi_item['cc'] = ','.join(sorted(tmp_cc))
                        spi_item['type'] = '0'
                        yield spi_item
                tmp_qs = ''
                tmp_cc = []

    def parse_ws(self, response):
        all_tr = response.css('table [border="1"] [width="100%"] tr')
        for x in all_tr:
            _tuple = get_tuple_by_ws(x.css('::text').extract())
            if _tuple[1]:
                date = get_date_by_qs(_tuple[0])
                if date:
                    spi_item = LhcSpiderItem()
                    spi_item['id'] = date[0]
                    spi_item['qs'] = date[1]
                    spi_item['year'] = date[2]
                    spi_item['month'] = date[3]
                    spi_item['day'] = date[4]
                    spi_item['cc'] = ','.join(_tuple[1])
                    spi_item['type'] = '1'
                    yield spi_item

    def parse_bs(self, response):
        all_tr = response.css('#table400921923 tr')
        for _bs_i, _bs_x in enumerate(all_tr):
            if _bs_i == 0:
                continue
            _tuple = get_tuple_by_bs(_bs_x.css('::text').extract())
            if _tuple[1]:
                date = get_date_by_qs(_tuple[0])
                if date:
                    spi_item = LhcSpiderItem()
                    spi_item['id'] = date[0]
                    spi_item['qs'] = date[1]
                    spi_item['year'] = date[2]
                    spi_item['month'] = date[3]
                    spi_item['day'] = date[4]
                    spi_item['cc'] = ','.join(_tuple[1])
                    spi_item['type'] = '2'
                    yield spi_item

    def parse_7x(self, response):
        all_tr = response.css('table tr')
        for i, x in enumerate(all_tr):
            if i == 0:
                continue
            _tuple = get_tuple_by_sx(x.css('::text').extract())
            if _tuple[1]:
                date = get_date_by_qs(_tuple[0])
                if date:
                    spi_item = LhcSpiderItem()
                    spi_item['id'] = date[0]
                    spi_item['qs'] = date[1]
                    spi_item['year'] = date[2]
                    spi_item['month'] = date[3]
                    spi_item['day'] = date[4]
                    spi_item['cc'] = ','.join(_tuple[1])
                    spi_item['type'] = '3'
                    yield spi_item

    def parse_3t(self, response):
        all_tr = response.css('table tr')
        for i, x in enumerate(all_tr):
            if i < 2:
                continue
            _tuple = get_tuple_by_3t(x.css('font::text').extract())
            if _tuple:
                date = get_date_by_qs(_tuple[0])
                if date:
                    spi_item = LhcSpiderItem()
                    spi_item['id'] = date[0]
                    spi_item['qs'] = date[1]
                    spi_item['year'] = date[2]
                    spi_item['month'] = date[3]
                    spi_item['day'] = date[4]
                    spi_item['cc'] = ','.join(_tuple[1])
                    spi_item['type'] = '4'
                    yield spi_item


