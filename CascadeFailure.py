# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 20:09:02 2020

@author: mohamad
"""


from InterdependentNetwork import InterdependentNetwork
from Reports import Reports

import numpy as np

class CascadeFailure:
    def __init__(self,numberOfNode,couplingStrength,totalPowerForEachNode,indexOfDayOfCascadingFailure):
        self.interdependentNetwork=InterdependentNetwork(numberOfNode,couplingStrength,totalPowerForEachNode)
        self.indexOfDayOfCascadingFailure=indexOfDayOfCascadingFailure #-1 if you don't want cascading failure
        self.reports=Reports()
        
    def distributePowerEqually(self,nodeEntity):
        neighbors=self.interdependentNetwork.getNeighborsOfSameNetworkNotFailedYet(nodeEntity)
        for i in range(0,len(neighbors)): 
            self.interdependentNetwork.getNetwork(nodeEntity).increaseCurrentPower(i,self.interdependentNetwork.getNetwork(nodeEntity).currentPower[nodeEntity.nodeIndex]/len(neighbors))
            
    def startSimulation(self,numberOfDays,assignPossibelityValue):
        self.assignPossibelityValue=assignPossibelityValue
        for dayIndedx in range(0,numberOfDays):
            if(self.indexOfDayOfCascadingFailure==dayIndedx):
                startCascadingFailureWithExtraPower()
            self.everyDayProcess()
        
        
    def everyDayProcess(self):
        nodes=self.interdependentNetwork.getListOfAllNode()
        for i in range(0,len(nodes)):
            self.AssignPowerOfThisDayToNodes(nodes[i])
            self.handlePowerOfThisDayToNodes(nodes[i])
        self.generateReportsForEveryDay() 
        
    def AssignPowerOfThisDayToNodes(self,nodeEntity):
        assignRandomValue = np.random.poisson(self.assignPossibelityValue, size=1)[0]
        self.interdependentNetwork.increaseCurrentPower(nodeEntity,assignRandomValue)
        
        
    def handlePowerOfThisDayToNodes(self,nodeEntity):
        self.interdependentNetwork.decreaseCurrentPowerForOneDay(nodeEntity)
        if self.interdependentNetwork.isNodeFail(nodeEntity):
            self.distributePowerEqually(nodeEntity)
            
    
    def generateReportsForEveryDay(self):
        self.reports.reportGiantComponent.append(self.interdependentNetwork.sizeOfGiantComponent())
        
      
    def startCascadingFailureWithExtraPower(self):
        self.interdependentNetwork.increaseCurrentPower(nodeEntity,assignRandomValue)
        
        
            
        

