#! /usr/bin/env python3
import loader

#load file config
configData = loader.ImportConfig()
htmlOut = configData['webconfig']['file']
webOn = configData['webconfig']['webserver']

#make file
filename = htmlOut

def webWrite(post):
    if webOn:
        target = open(filename, 'a') #append to html file
        target.write("<BR><a href='" + post.link + "'>" + post.title + "</a><BR>")
        target.close()
    else:
        print("Webserver function is not set to true in your config.")