#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: tnhung2011
# email: nhathungtran2011@gmail.com

from webbrowser import open
from os import startfile
from os.path import isfile
from os.path import exists


def start(path, raiseError=False):
    __920834029384084 = None
    
    if exists(path):
        if raiseError is False:
            return True        
        
        if isfile():
            startfile(path)
        else:
            open(path)
    else:
        __920834029384084 = open(path)
        if __920834029384084 is False:
            if raiseError is True:
                raise TypeError("FileNotExist")
            else:
                return False

def exists(path):
    if exists(path):
        return True
    else:
        return False
