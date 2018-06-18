import pandas as pd
import numpy as np
from pulp import *
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

def Data(ResponseTime):
    """ Import Data And form File Pop and Time
    and also convert time data to binary time data according
    to threshold value of Response time
    """
    
    Population=pd.read_csv('pop.txt',sep='  ',header=None,names=['loc','pop'],engine='python')
    Population.set_index('loc', inplace=True) # population data
    
    TimeMat=pd.read_csv('time.txt',sep=' ',header=None) # Time data matrix
    
    
    del TimeMat[40]
    
    BoolData=TimeMat<= ResponseTime # binary data according to given response time
    BoolDataN=BoolData*1
   
    return (BoolDataN.values,Population)


def EMSFunc(ResponseTime):
    """  using puLP module find No. of ambulance require
    """
    
    TimeBinaryData , PopulationData = Data(ResponseTime)

    
    prob = pulp.LpProblem('AmbulanceLocation', pulp.LpMinimize)
    
    AmbulanceLocation = range(40)
    
    # Variable
    x = LpVariable.dicts('x',AmbulanceLocation ,upBound=1, lowBound=0,cat=pulp.LpInteger)
    
    # Objective function   
    prob += lpSum(x[i] for i in AmbulanceLocation)
    
    # constraints
    for i in range(85):
            prob += lpSum(TimeBinaryData[i,j]*x[j] for j in range(40) ) >=1
    prob.solve()
   
    if  LpStatus[prob.status] != 'Optimal':
        return None
    else:
        return (value(prob.objective))

    

   
print("programme is running....")
A=np.empty(17)
for i in range(4,21):   
    A[i-4]=EMSFunc(i)
x=list(range(4,21))
plt.scatter(x,A)
plt.xlabel("Response Time Bound")
plt.ylabel("No. of Ambulance")
plt.show()

