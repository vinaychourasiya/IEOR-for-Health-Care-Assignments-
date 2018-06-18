import numpy as np
import matplotlib.pyplot as plt
from math import *
from pulp import *

A =np.zeros((121,121))
"""
'A' is a complete pixel matrix that contain different
intensities of organ and tumor 
"""
for i in range(121):
    for j in range(121):
        dist=((i-60)**2+(j-60)**2)**.5
        if dist<=60:
            A[i][j]+=4
for i in  range(30,91):
    for j in range(20,41):
        A[j][i]=10
for i in  range(50,71):
    for j in range(40,81):
        A[j][i]=10
for i in  range(30,91):
    for j in range(80,101):
        A[j][i]=10
"""
D0 matrix dose matrix coresponding to I section
with intensity 1
"""


D0=np.zeros((121,121))
for i in range(50,71):
    for j in range(120):
        if A[j][i]!= 0:
            x = j/20                # x = distance of beam from start
            D0[j][i]= 1/(2**(x/4))  # decay update with distance of beam

def Dose(D,theta):
    """
    function for creating angle
    for 1cm Beam with the use
    of Rotational Matrix update
    """
    d1=np.zeros((121,121))
    for i in range(50,70):
        for j in range(120):
            if D[j][i]!= 0:
                a=np.radians(theta)
                i1=int(np.floor((i-60)*np.cos(a)-(j-60)*np.sin(a)))+60 #i1,j1 is new indices after rotation of theta angle
                j1=int(np.floor((i-60)*np.sin(a)+(j-60)*np.cos(a)))+60
                d1[j1][i1]= D[j][i]
    for i in range(120):
        for j in range(120):
            if d1[j][i]==0:
                d1[j][i]= (d1[j][i+1]+d1[j-1][i])/2
    return d1

"""
Dose Matrix At different different angle
D180 mean Dose matrix of 180'
"""

D180=Dose(D0,180)
D30=Dose(D0,30)
D210=Dose(D0,210)
D330=Dose(D0,330)
D150=Dose(D0,150)
D45=Dose(D0,45)
D225=Dose(D0,225)
D135=Dose(D0,135)
D315=Dose(D0,315)
D_vec=np.array([D210,D30,D0,D180,D330,D150,D45,D225,D135,D315])
Dsum=(D210+D30+D0+D330+D150+D45+D225+D135+D315+D180)*4
print("Mutibeam fired with different angle")
plt.pcolor(Dsum,cmap='RdGy')
plt.colorbar()
plt.title("Mutibeam fired at different angle with same intensity 4" )
plt.show()

#==================PULP Solution===========================#

prob = pulp.LpProblem('LP1', pulp.LpMinimize)
    
# Define variable
N= range(10)
w = LpVariable.dicts('w',N,upBound=None, lowBound=0,cat=pulp.LpContinuous)
pixel = [(i, j) for i in range(121) for j in range(121)]
D = LpVariable.dicts('D',pixel,upBound=None, lowBound=0,cat=pulp.LpContinuous)
    
# Objective Function
prob += lpSum(D[(i,j)] for i in range(121) for j in range(121) )
   
# Constraints
for i in range(121):
    for j in range(121):
        prob+= lpSum(w[p]*D_vec[p][j][i] for p in range(10))==D[(j,i)]
        
for i in range(121):
    for j in range(121):
        if A[j][i]==10:
            prob += lpSum(D[(j,i)]) >= 10
        else:
            prob += lpSum(D[(j,i)]) <= 4
    
prob.solve()    
# Status of Given Programme  
print ("Status of LP :", LpStatus[prob.status])




