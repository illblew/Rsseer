#! /usr/bin/env python3
import loader

#load file config
configData = loader.ImportConfig()
htmlOut = configData['webconfig']['file']
webOn = configData['webconfig']['webserver']
title = configData['webconfig']['title']
inject = configData['webconfig']['inject']
with open ("bootHTML.cfg", "r") as bootFile:
    bootHTML = bootFile.readlines()

#make file
filename = htmlOut

def webWrite(post):
    if webOn:
        target = open(filename, 'a') #append to html file
        target.write("<td class='info'><a href='" + post.link + "' target='_new'>" + post.title + "</a></td></tr>")
        target.close()
    else:
        print("Webserver function is not set to true in your config.")

def injector():
    bootConv = str(bootHTML).replace("'\n'"," ")
    target = open(filename, 'a') #append to html file
    target.write("<head><title>" + title + "</title> <font color='white'> " + bootConv + "</font></head><body><font size='2'><b><div class='container'><center><img src='images/logo.jpg'></center><table class='table'><tr><th class='warning'>Your Feed</th><tbody><tr class='info'>")
    target.close()
