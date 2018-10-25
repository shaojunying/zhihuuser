# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    start_user = 'shao-jun-ying-40'

    user_url = 'https://www.zhihu.com/api/v4/members/{username}?include={include}&offset=0&limit=20'
    user_query_params = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,' \
                        'badge[?(type=best_answerer)].topics '

    followers_url = 'https://www.zhihu.com/api/v4/members/{username}/followers?include={include}&offset={offset}&limit={limit} '

    followers_params = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,' \
                       'badge[?(type=best_answerer)].topics '

    def start_requests(self):
        yield Request(url=self.user_url.format(username=self.start_user,
                                               include=self.user_query_params),
                      callback=self.parse_user)
        yield Request(url=self.followers_url.format(username=self.start_user,
                                                    include=self.followers_params,
                                                    offset=0, limit=20),
                      callback=self.parse_follows)

    @staticmethod
    def parse_user(response):
        print(response.text)
        pass

    def parse_follows(self, response):
        # print(response.text)
        pass
