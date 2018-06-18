import pandas as pd
import numpy as np
from pulp import *


def Data(ResponseTime):
    """ Import Data And form File Pop and Time
    and also convert time data to binary time data according
    to threshold value of Response time
    """
    Population=pd.read_csv('pop.txt',sep='  ',header=None,names=['loc','pop'],engine='python')
    Population.set_index('loc', inplace=True)
    pop=Population.values
    
    TimeMat=pd.read_csv('time.txt',sep=' ',header=None) # time data  matrix
    
    del TimeMat[40]
    BoolData=TimeMat <= ResponseTime # converting into binary data according to given response time
    BoolDataN=BoolData*1
    
    return (BoolDataN.values,pop.flatten()) # return Array of Time binary data and population data


def EMSFunc(ResponseTime):
    
    """  using puLP module find No. of ambulance require
    """
    
    TimeBinaryData , PopulationData = Data(ResponseTime) # extracting data from Data function
    
    prob = pulp.LpProblem('AmbulanceLocation', pulp.LpMinimize)
    
    AmbulanceLocation = range(40)
    
    # Define variable   
    x = LpVariable.dicts('x',AmbulanceLocation ,upBound=1, lowBound=0,cat=pulp.LpInteger)
    
    
    # Objective Function 
    prob += lpSum(x[i] for i in AmbulanceLocation)
    
    # Constraints 
    for i in range(85):
            prob += lpSum(TimeBinaryData[i,j]*x[j] for j in range(40) ) >=1
    
    
    prob.solve()
    
    # Status of Given Programme
    
    print ("Status:", LpStatus[prob.status])
   
    
    print ("minimum number of ambulances required = ", value(prob.objective))
            
    for candLoc in AmbulanceLocation:
        if x[candLoc].varValue==1:
            print("Ambulance  Location = " ,candLoc+1)
   
EMSFunc(10)

    
