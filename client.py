#! /usr/bin/env python3
import feedparser,loader,ssl

#get the config data
configData = loader.ImportConfig()

#set interval
interval = configData['config']['interval']
#set feed url
url = configData['config']['url']
#ssl patch for feedparser
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def StartClient():
    rData = FeedCheck(url,interval)
    for post in rData.entries:
        print(Color.BOLD + Color.GREEN + post.title + "\n"+ Color.RED + post.link + "\n")

def FeedCheck(url,interval):
    feed = feedparser.parse(url)
    return feed