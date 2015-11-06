#! /usr/bin/env python3
import yaml

configFile = "config.yaml"

def ImportConfig():
    with open(configFile,'r') as stream:
        yamlData = yaml.load(stream)
        return yamlData