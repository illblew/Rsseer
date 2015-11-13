#! /usr/bin/env python3
import feedparser,loader,ssl,threading,time,htmler,os



#get the config data
configData = loader.ImportConfig()

#set feed url
url = configData['config']['url']

#interval get
interval = configData['config']['interval']

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
    if os.path.isfile(htmler.filename):
        os.remove(htmler.filename)
    print(chr(27) + "[2J")
    rData = FeedCheck(url)
    for post in rData.entries:
        print(Color.BOLD + Color.GREEN + post.title + "\n"+ Color.RED + post.link + "\n")
        htmler.webWrite(post)
    Start()

def FeedCheck(url):
    feed = feedparser.parse(url)
    return feed

def Start():
    time.sleep(5)
    threading.Timer(interval,StartClient).start()

StartClient()
