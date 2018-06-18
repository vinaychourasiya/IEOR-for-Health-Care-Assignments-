import numpy as np


def Simulation(N,parameter):
    alpha,theta=parameter
    PatientTime=np.zeros(100000)
    DoctorTime=np.zeros(100000)
    for i in range(100000):

        D_WaitingTime=np.zeros(N)
        P_WaitingTime=np.zeros(N)
        
        S1=np.arange(0,N*12,24)
        S2=np.arange(0,N*12,24)
        ScheduledTime=np.hstack(zip(S1,S2))
        
        
        ActualServTime=np.random.gamma(alpha,theta,N)
        CompeletedTime=np.zeros(N)
        
        for patient in range(N):
            
            if patient==0:                                      #for 1st patient
                CompeletedTime[patient]=ActualServTime[patient]
            else:
                if CompeletedTime[patient-1] < ScheduledTime[patient]:
                    D_WaitingTime[patient]=max(ScheduledTime[patient]-CompeletedTime[patient-1],0)
                    
                    CompeletedTime[patient]=ActualServTime[patient]+CompeletedTime[patient-1]+D_WaitingTime[patient]
                
                elif CompeletedTime[patient-1] >= ScheduledTime[patient]:
                    P_WaitingTime[patient]=CompeletedTime[patient-1]-ScheduledTime[patient]
                    
                    CompeletedTime[patient]=ActualServTime[patient]+CompeletedTime[patient-1]
        PatientTime[i]=np.sum(P_WaitingTime)
        DoctorTime[i]=np.sum(D_WaitingTime)
    #print(ScheduledTime)
    return (np.mean(PatientTime),np.mean(DoctorTime))


parameter=(16,3/4)
N=30      
AvgPatientWait,AvgDrWait = Simulation(N, parameter)   
print("Average waiting times of all patients: ", AvgPatientWait)
print("the average time the practitioner is idle: ",AvgDrWait)
  
  

  
