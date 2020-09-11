# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 00:23:08 2020

@author: mohamad
"""


from CascadeFailure import CascadeFailure

ourSimulation=CascadeFailure(numberOfNode=100,
                             couplingStrength=1.0,
                             totalPowerForEachNode=100)
assignPossibelityValue=90
numberOfDays=10
numberOfNodeForCascadingFailure=40
numberOfNodesForRestoration=40
sizeOfGiantAtTheEndOfEachCase=[]
for i in range(0,numberOfDays):
        ourSimulation.startSimulation(numberOfDays=numberOfDays,
        assignPossibelityValue=assignPossibelityValue,
        indexOfDayOfCascadingFailure=8,
        numberOfNodeForCascadingFailure=numberOfNodeForCascadingFailure,
        numberOfNodesForRestoration=numberOfNodesForRestoration,
        indexOfDayOfZhongRestoration=-1) 
        sizeOfGiantAtTheEndOfEachCase.append(ourSimulation.giantAtTheEnd)
    
ourSimulation.reports.plotChartGiantComponent(sizeOfGiantAtTheEndOfEachCase)