# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 15:55:38 2020

@author: mohamad
"""


from ScaleFree import ScaleFreeNetwork
from nodeEntity import NodeEntity
from Utils import getKeysByValue
from Utils import getColumnsFromList
import random
from Reports import Reports


class InterdependentNetwork:
    def __init__(self,numberOfNode,couplingStrength,totalPowerForEachNode):
        self.network1=ScaleFreeNetwork(numberOfNode,totalPowerForEachNode)
        Reports().plotGraphScaleFree(self.network1.graph)
        self.network2=ScaleFreeNetwork(numberOfNode,totalPowerForEachNode)
        Reports().plotGraphScaleFree(self.network2.graph)
        self.makingConnectionBetweenTwoNetworks(couplingStrength)
    
    def makingConnectionBetweenTwoNetworks(self,couplingStrength):
        self.connectionBetweenNetworks=[]
        self.couplingStrength = couplingStrength             
        randomList1=self.network1.getNodes()
        random.shuffle(randomList1)
        randomList2=self.network2.getNodes()
        random.shuffle(randomList2)
        numberOfCouple=int(self.couplingStrength*len(self.network1.getNodes()))
        for i in range(0,int(numberOfCouple)):
            self.connectionBetweenNetworks.append([randomList1[i],randomList2[i]])
        
    def getNetwork(self,nodeEntity):
        return self.getNetworkWithIndex(nodeEntity.networkIndex)
    
    def getAnotherNetwork(self,nodeEntity):
        return self.getAnotherNetworkWithIndex(nodeEntity.networkIndex)
    
    def getNetworkWithIndex(self,networkIndex):
        if networkIndex==1:
            return self.network1
        if networkIndex==2:
            return self.network2
        
    def getAnotherNetworkWithIndex(self,networkIndex):
        if networkIndex==1:
            return self.network2
        if networkIndex==2:
            return self.network1
        
    def isNodeFail(self,nodeEntity):
        if self.getNetwork(nodeEntity).isNodeFail(nodeEntity.nodeIndex):
            return True
        if self.getAnotherNetwork(nodeEntity).isNodeFail(nodeEntity.nodeIndex):
            return True
        return False
    
    def findingCentrality(self,numberOfCenralityNode):
        centalNetwork1=self.network1.findingCentrality(numberOfCenralityNode)
        centalNetwork2=self.network2.findingCentrality(numberOfCenralityNode)
        output=[]
        for i in range(0,numberOfCenralityNode):
            if(centalNetwork1[0][1]>centalNetwork1[0][1]):
                output.append(NodeEntity(1, centalNetwork1[0][0]))
                centalNetwork1.pop(0)
            else:
                output.append(NodeEntity(2, centalNetwork2[0][0]))
                centalNetwork2.pop(0)
                
        return output
                
    
    def getNeighborsOfSameNetworkNotFailedYet(self,nodeEntity):
        output=[]
        neighbors=self.getNetwork(nodeEntity).getNeighbors(nodeEntity.nodeIndex)
        for i in range(0,len(neighbors)):
            if self.isNodeFail(NodeEntity(nodeEntity.networkIndex,neighbors[i]))==False:
                output.append(NodeEntity(nodeEntity.networkIndex,neighbors[i]))
        return output
    
    def getCouple(self,nodeEntity):
        coulmnOfConnection=getColumnsFromList(self.connectionBetweenNetworks,nodeEntity.networkIndex-1)
        if nodeEntity.nodeIndex in coulmnOfConnection:
            couple=self.connectionBetweenNetworks[coulmnOfConnection.index(nodeEntity.nodeIndex)]
            if nodeEntity.networkIndex==1:
                return NodeEntity(2, couple[1])
            else:
                return NodeEntity(1, couple[0])
            
    def hasCouple(self,nodeEntity):
        coulmnOfConnection=getColumnsFromList(self.connectionBetweenNetworks,nodeEntity.networkIndex-1)
        return nodeEntity.nodeIndex in coulmnOfConnection
            
    def getNeighborsOfTotalNetworkNotFailedYet(self,nodeEntity):
        neighbors=self.getNeighborsOfSameNetworkNotFailedYet(nodeEntity)
        if self.hasCouple(nodeEntity):
            neighbors.append(self.getCouple(nodeEntity))
        return neighbors
            
    
    def getListOfAllNode(self):
        output=[]
        nodeListNetwork1=self.network1.getNodes()
        for i in range(0,len(nodeListNetwork1)):
            output.append(NodeEntity(1,nodeListNetwork1[i]))
            
        nodeListNetwork2=self.network2.getNodes()
        for i in range(0,len(nodeListNetwork2)):
            output.append(NodeEntity(2,nodeListNetwork2[i]))
        return output
    
    def increaseCurrentPower(self,nodeEntity,value):
        self.getNetwork(nodeEntity).increaseCurrentPower(nodeEntity.nodeIndex,value)
    
    def decreaseCurrentPowerForOneDay(self,nodeEntity):
        self.getNetwork(nodeEntity).decreaseCurrentPowerForOneDay(nodeEntity.nodeIndex)

    def getUniqueIdWithNodeEntity(self,nodeEntity):
        return (nodeEntity.networkIndex*10000)+nodeEntity.nodeIndex
    
    def getNodeEntityWithUniqueId(self,uniqueId):
        return NodeEntity((int)(uniqueId/10000),uniqueId%10000)
        
    def sizeOfGiantComponent(self):
        visitedNodeEntity = {}
        
        nodeListNetworks=self.getListOfAllNode()
    
        for i in range(0,len(nodeListNetworks)):
            visitedNodeEntity[self.getUniqueIdWithNodeEntity(nodeListNetworks[i])]=False
        
        stackOfDfsNodeEntity=[]
        sizeOfMaxComponent=0;
        while len(getKeysByValue(visitedNodeEntity,False))>0:
            sizeOfCurrentComponent=0;
            stackOfDfsNodeEntity.append(self.getNodeEntityWithUniqueId(getKeysByValue(visitedNodeEntity,False)[0]))
            
            while len(stackOfDfsNodeEntity)>0:
                currentNode=stackOfDfsNodeEntity.pop()
                #for i in range(0,len(visitedNodeEntity)):
                    #print(i)
                    #print(i," netwrok ",visitedNodeEntity[i].networkIndex," node ",visitedNodeEntity[i].nodeIndex)
                #print(visitedNodeEntity[currentNode])
                if visitedNodeEntity[self.getUniqueIdWithNodeEntity(currentNode)]==True:
                    continue
                visitedNodeEntity[self.getUniqueIdWithNodeEntity(currentNode)]=True
                sizeOfCurrentComponent += 1
                if sizeOfCurrentComponent > sizeOfMaxComponent:
                    sizeOfMaxComponent = sizeOfCurrentComponent
                
                neighborNodes = self.getNeighborsOfTotalNetworkNotFailedYet(currentNode)
                stackOfDfsNodeEntity.extend(neighborNodes)
            
                
        return sizeOfMaxComponent/(len(self.getListOfAllNode()))