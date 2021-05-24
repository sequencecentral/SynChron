#!/bin/python
import unittest
import json

import synchron
# print(dir(synchron))
from synchron import utils
from synchron import quotewidget
from synchron import redditwidget
from synchron import newswidget
from synchron import rsswidget
from synchron import udemywidget

class POC(unittest.TestCase):
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class Utils(unittest.TestCase):
    def test_get_item(self,str="one two three"):
        item = utils.get_item(str)
        self.assertEqual(type(item),type("text"))

    def test_timestamp(self):
        item = utils.timestamp()
        self.assertEqual(type(item),type("text"))
    
    def test_clean_text(self,str="<html>Test&hey!!!"):
        item = utils.clean_text(str)
        self.assertEqual(type(item),type("text"))
    
    def test_format_tweet(self,ti="tweet_title",url="https://example.com",summary="",intro="",bebukey=None):
        print("Testing tweet:")
        tw = utils.format_tweet(ti,url,summary,intro,bebukey)
        print(tw)
        self.assertEqual(type(tw['tweet']),type("text"))

class QuoteWidget(unittest.TestCase):
    def test_get_post(self):
        post = quotewidget.create_post()
        # print(post)
        self.assertEqual(type(post['tweet']),type("text"))
    
    def test_get_posts(self):
        count = 3
        posts = quotewidget.get_posts(None,count)
        # print(posts)
        self.assertEqual(count,len(posts))
        self.assertEqual(type(posts[0]['tweet']),type("text"))

class RedditWidget(unittest.TestCase):
    def test_get_posts(self):
        with open("env.json","r") as creds:
            env = json.load(creds)
            # print(env)
            count=1
            posts = redditwidget.get_posts(env,count,subreddit="worldnews")
            print(posts)

class NewsWidget(unittest.TestCase):
    def test_get_posts(self):
        posts = newswidget.get_posts({},1,term = "news")
        print(posts)

class RSSWidget(unittest.TestCase):
    def test_get_posts(self):
        posts = rsswidget.get_posts({},1,feed = "genomics")
        print(posts)

class UdemyWidget(unittest.TestCase):
    def test_get_posts(self):
        with open("env.json","r") as creds:
            env = json.load(creds)
            # print(env)
            count=1
            posts = udemywidget.get_posts(env,count)
            print(posts)

if __name__ == '__main__':
    unittest.main(RedditWidget())