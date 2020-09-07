# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 00:23:08 2020

@author: mohamad
"""


from CascadeFailure import CascadeFailure

ourSimulation=CascadeFailure(numberOfNode=20,
                             couplingStrength=1.0,
                             totalPowerForEachNode=100)


ourSimulation.startSimulation(numberOfDays=20,
                              assignPossibelityValue=98,
                              indexOfDayOfCascadingFailure=1,
                              numberOfNodeForCascadingFailure=10)

ourSimulation.reports.plotChartGiantComponent()
