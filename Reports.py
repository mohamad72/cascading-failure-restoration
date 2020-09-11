# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 21:21:47 2020

@author: mohamad
"""
import matplotlib.pyplot as plt
import networkx as nx


class Reports:
        
    def plotChartGiantComponent(self):
        self.plotChartGiantComponent(self.reportGiantComponent)
        
    def plotChartGiantComponent(self,listOfChart):
        plt.ylim(top=1.05)
        plt.ylim(bottom=-0.05)
        plt.plot(listOfChart)
        plt.show()
     
    def plotMultiChartGiantComponent(self,numberOfRestore,listOfChart):
        plt.ylim(top=1.05)
        plt.ylim(bottom=-0.05)
        for i in range(0,len(listOfChart)):
            plt.plot(listOfChart[i])
        plt.gca().legend(('R={} '.format(numberOfRestore[0]),'R={} '.format(numberOfRestore[1]),'R={} '.format(numberOfRestore[2]),'R={} '.format(numberOfRestore[3])))
        plt.plot(listOfChart)
        plt.show()
        
    def setReportGiantComponent(self):
        self.reportGiantComponent=[]
        
        
    def plotGraphScaleFree(self,graph):
        nx.draw(graph,with_labels=True)
        plt.show()
        
        
    def networkCurrentPower(self,currentPower1,currentPower2):
        print(currentPower1,currentPower2)
    
    