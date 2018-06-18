import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
np.random.seed(1111)

def WaitTimeSimulation(parameter):
    # parameter for gamma
    k,lemda=parameter 
    serviceTime=np.ones(100000)
    for j in range(100000):
        ServTime=np.random.gamma(k,lemda)
        serviceTime[j]=ServTime
    AvgServTime=np.mean(serviceTime)
    print("waiting time of the second patient to get service : ",AvgServTime)
    return serviceTime
    
param=(16,3/4)
serviceTime=WaitTimeSimulation(param)

plt.hist(serviceTime, bins=40)
plt.vlines(x=np.mean(serviceTime), ymin=0, ymax=9500, colors='red')
plt.xlabel("Waiting Time of 2nd patient")
plt.ylabel("Frequency")
plt.savefig("histogram")
plt.show()    
        
        

    
       
    
    
    
