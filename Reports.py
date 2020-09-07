# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 21:21:47 2020

@author: mohamad
"""
import matplotlib.pyplot as plt
import networkx as nx


class Reports:
        
    def plotChartGiantComponent(self):
        plt.ylim(top=1.05)
        plt.ylim(bottom=-0.05)
        plt.plot(self.reportGiantComponent)
        plt.show()
        
        
    def setReportGiantComponent(self):
        self.reportGiantComponent=[]
        
        
    def plotGraphScaleFree(self,graph):
        nx.draw(graph,with_labels=True)
        plt.show()
        
        
    def networkCurrentPower(self,currentPower1,currentPower2):
        print(currentPower1,currentPower2)
    
    