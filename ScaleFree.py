# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 14:50:57 2020

@author: mohamad
"""
import matplotlib.pyplot as plt
import networkx as nx
import networkx.algorithms.centrality as centrality

class ScaleFreeNetwork:
    def __init__(self,numberOfNode,totalPowerForEachNode):
        self.graph = nx.powerlaw_cluster_graph(numberOfNode,(int)(numberOfNode/10),0.1)
        self.currentPower=[0]*numberOfNode
        self.totalPower=[totalPowerForEachNode]*numberOfNode
        self.MeanPower=[0]*numberOfNode
        
    def plotGraphScaleFree(self):
        nx.draw(self.graph,with_labels=True)
        plt.show()
        
    def isNodeFail(self,nodeIndex):
        return self.currentPower[nodeIndex]>self.totalPower[nodeIndex]
    
    def getNeighbors(self,nodeIndex):
        return [n for n in self.graph.neighbors(nodeIndex)] 
    
    def getNumberOfNeighbors(self,nodeIndex):
        return len(self.getNeighbors(nodeIndex))
    
    def getNodes(self):
        return list(self.graph.nodes)
    
    def setMeanPower(self,nodeIndex,meanPower):
        self.MeanPower[nodeIndex]=meanPower
    
    def getMeanPower(self,nodeIndex):
        return self.MeanPower[nodeIndex]
    
    def increaseCurrentPower(self,nodeIndex,value):
        self.currentPower[nodeIndex]+=value
    
    def decreaseCurrentPower(self,nodeIndex,value):
        self.currentPower[nodeIndex]-=value
        if self.currentPower[nodeIndex]<0:
            self.currentPower[nodeIndex]=0
    
    def decreaseCurrentPowerForOneDay(self,nodeIndex):
        self.decreaseCurrentPower(nodeIndex,self.totalPower[nodeIndex])
        
    