# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 21:21:47 2020

@author: mohamad
"""
import matplotlib.pyplot as plt


class Reports:
    def __init__(self):
        self.reportGiantComponent=[]
        
    def plotChartGiantComponent(self):
        plt.ylim(top=1.05)
        plt.ylim(bottom=-0.05)
        plt.plot(self.reportGiantComponent)
        plt.show()
    
    