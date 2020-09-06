# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 02:19:41 2020

@author: mohamad
"""


def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys


def getColumnsFromList(inputList, columnIndex):
    output=[]
    for i in range(0,len(inputList)):
        output.append(inputList[i][columnIndex])
    return  output