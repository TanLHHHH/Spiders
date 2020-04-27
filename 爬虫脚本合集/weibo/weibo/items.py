# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CommentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 评论时间
    comment_time = scrapy.Field()
    # 评论文本
    text = scrapy.Field()
    # 评论人id
    comment_people_id = scrapy.Field()
    # 评论人name
    comment_people_name = scrapy.Field()
    # 评论点赞数
    comment_likes = scrapy.Field()
    # 评论回复总数
    total_number = scrapy.Field()

class PeopleItem(scrapy.Item):
    name = scrapy.Field()
    user_id = scrapy.Field()
    # 关注数
    follow_count = scrapy.Field()
    # 粉丝数
    followers_count = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 微博数
    statuses_count = scrapy.Field()
    # 是否认证
    verified = scrapy.Field()
    # 认证缘由
    verified_reason = scrapy.Field()
    
    
class StatusesItem(scrapy.Item):
    edit_at = scrapy.Field()
    text = scrapy.Field()
    reposts_count = scrapy.Field()
    comments_count = scrapy.Field()
    attitudes_count = scrapy.Field()
    statues_id = scrapy.Field()
    origin_url = scrapy.Field()
    
    # edit_at = data['mblog']['created_at']
    # text = data['mblog']['text']
    # reposts_count = data['mblog']['reposts_count']
    # comments_count = data['mblog']['comments_count']
    # attitudes_count = data['mblog']['attitudes_count']
    # statues_id = data['mblog']['id']
    # origin_url = data['scheme'].split('?')[0