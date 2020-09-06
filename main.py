# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 00:23:08 2020

@author: mohamad
"""


from CascadeFailure import CascadeFailure

ourSimulation=CascadeFailure(numberOfNode=200,couplingStrength=1.0,totalPowerForEachNode=100)

ourSimulation.startSimulation(numberOfDays=20,assignPossibelityValue=95)

ourSimulation.reports.plotChartGiantComponent()
