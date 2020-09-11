# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 20:09:02 2020

@author: mohamad
"""


from InterdependentNetwork import InterdependentNetwork
from Reports import Reports
from nodeEntity import NodeEntity
from ScaleFree import ScaleFreeNetwork

import numpy as np

class CascadeFailure:
    def __init__(self,numberOfNode,couplingStrength,totalPowerForEachNode):
        self.numberOfNode=numberOfNode
        self.interdependentNetwork=InterdependentNetwork(numberOfNode,couplingStrength,totalPowerForEachNode)
        self.reports=Reports()
        
            
    def startSimulation(self,
                        numberOfDays,
                        assignPossibelityValue,
                        indexOfDayOfCascadingFailure,
                        numberOfNodeForCascadingFailure,
                        numberOfNodesForRestoration,
                        indexOfDayOfZhongRestoration):
        self.numberOfNodesForRestoration=numberOfNodesForRestoration
        self.interdependentNetwork.network1.currentPower=[0]*self.numberOfNode
        self.interdependentNetwork.network2.currentPower=[0]*self.numberOfNode
        self.indexOfDayOfZhongRestoration=indexOfDayOfZhongRestoration
        self.numberOfNodeForCascadingFailure=numberOfNodeForCascadingFailure
        self.reports.setReportGiantComponent()
        self.indexOfDayOfCascadingFailure=indexOfDayOfCascadingFailure #-1 if you don't want cascading failure
        self.assignPossibelityValue=assignPossibelityValue
        for dayIndedx in range(0,numberOfDays):
            if(self.indexOfDayOfCascadingFailure==dayIndedx):
                self.startCascadingFailureWithExtraPowerToCentralNode()
            if(self.indexOfDayOfZhongRestoration==dayIndedx):
                self.startRestoratinZhongWithDoingEmptyOfCentralNode()
            self.everyDayProcess()
        self.giantAtTheEnd=self.interdependentNetwork.sizeOfGiantComponent()
        
        
        
    def everyDayProcess(self):
        nodes=self.interdependentNetwork.getListOfAllNode()
        for i in range(0,len(nodes)):
            self.AssignPowerOfThisDayToNodes(nodes[i])
        for i in range(0,len(nodes)):
            self.handlePowerOfThisDayToNodes(nodes[i])
        self.listOfNewFailes=[]
        for i in range(0,len(nodes)):
            self.decitionAboutDistributePower(nodes[i])
        for i in range(0,len(self.listOfNewFailes)):
            self.distributePowerEqually(self.listOfNewFailes[i][0],self.listOfNewFailes[i][1]) 
            #self.distributePowerExprimentaly(self.listOfNewFailes[i][0],self.listOfNewFailes[i][1]) 

    def AssignPowerOfThisDayToNodes(self,nodeEntity):
        assignRandomValue = np.random.poisson(self.assignPossibelityValue, size=1)[0]
        assignRandomValue=90
        self.interdependentNetwork.increaseCurrentPower(nodeEntity,assignRandomValue)
        
        
    def handlePowerOfThisDayToNodes(self,nodeEntity):
        self.interdependentNetwork.decreaseCurrentPowerForOneDay(nodeEntity)
        
        
    def decitionAboutDistributePower(self,nodeEntity):
        if self.interdependentNetwork.isNodeFail(nodeEntity):
            totalPowerOfThisNode=self.interdependentNetwork.getNetwork(nodeEntity).currentPower[nodeEntity.nodeIndex]
            self.listOfNewFailes.append([nodeEntity,totalPowerOfThisNode]) 
    
    def distributePowerEqually(self,nodeEntity,totalPower):
        neighbors=self.interdependentNetwork.getNeighborsOfSameNetworkNotFailedYet(nodeEntity)
        if(len(neighbors)>0 and totalPower>0):
            for i in range(0,len(neighbors)): 
                self.interdependentNetwork.increaseCurrentPower(NodeEntity(nodeEntity.networkIndex,neighbors[i].nodeIndex),(int)(totalPower/len(neighbors)))
            self.interdependentNetwork.getNetwork(nodeEntity).currentPower[nodeEntity.nodeIndex]=0
    
    def distributePowerExprimentaly(self,nodeEntity,totalPower):
        neighbors=self.interdependentNetwork.getNeighborsOfSameNetworkNotFailedYet(nodeEntity)
        if(len(neighbors)>0 and totalPower>0):
            neighborsVulnerability=self.interdependentNetwork.getVulnerabilityOfSomeNodeEntities(neighbors)
            sumOfCoefs=sum(neighborsVulnerability)
            for i in range(0,len(neighbors)): 
                self.interdependentNetwork.increaseCurrentPower(NodeEntity(nodeEntity.networkIndex,neighbors[i].nodeIndex),(int)((totalPower*neighborsVulnerability[i])/sumOfCoefs))
            self.interdependentNetwork.getNetwork(nodeEntity).currentPower[nodeEntity.nodeIndex]=0
                
    def generateReportsForEveryDay(self):
        sizeOfGiantComponent=self.interdependentNetwork.sizeOfGiantComponent()
        self.reports.reportGiantComponent.append(sizeOfGiantComponent)
        currentPower1List=self.interdependentNetwork.network1.currentPower
        currentPower2List=self.interdependentNetwork.network2.currentPower
        self.reports.networkCurrentPower(currentPower1List,currentPower2List)
        

    def startCascadingFailureWithExtraPowerToCentralNode(self):
        assignExtraValue = 200
        centralNodes=self.interdependentNetwork.findingCentrality(self.numberOfNodeForCascadingFailure)
        for i in range(0,len(centralNodes)):
            self.interdependentNetwork.increaseCurrentPower(centralNodes[i],assignExtraValue)
        
    def startRestoratinZhongWithDoingEmptyOfCentralNode(self):
        centralNodes=self.interdependentNetwork.findingCentrality(self.numberOfNodesForRestoration)
        for i in range(0,len(centralNodes)):
            self.interdependentNetwork.getNetwork(centralNodes[i]).currentPower[centralNodes[i].nodeIndex]=0

            
        

