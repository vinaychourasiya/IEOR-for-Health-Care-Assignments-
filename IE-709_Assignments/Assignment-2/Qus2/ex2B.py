import numpy as np

def Simulation(N,parameter):
    alpha,theta=parameter
    PatientTime=np.zeros(100000)
    DoctorTime=np.zeros(100000)
    for i in range(100000):
    
        D_WaitingTime=np.zeros(N)
        P_WaitingTime=np.zeros(N)
        ScheduledTime=np.arange(0,N*12,12)
        ScheduledTime=np.concatenate((np.zeros(1),ScheduledTime))
        ActualServTime=np.random.gamma(alpha,theta,N)
        CompeletedTime=np.zeros(N)
        
        for patient in range(N):
            if patient==0:
                CompeletedTime[patient]=ActualServTime[patient]
            elif patient==1:
                P_WaitingTime[patient]=CompeletedTime[[patient-1]]
                CompeletedTime[patient]=ActualServTime[patient]+CompeletedTime[patient-1]
            else:
                if CompeletedTime[patient-1] < ScheduledTime[patient]:
                    D_WaitingTime[patient]=ScheduledTime[patient]-CompeletedTime[patient-1]
                    
                    CompeletedTime[patient]=ActualServTime[patient]+CompeletedTime[patient-1]+D_WaitingTime[patient]
                
                elif CompeletedTime[patient-1] >= ScheduledTime[patient]:
                    P_WaitingTime[patient]=CompeletedTime[patient-1]-ScheduledTime[patient]
                    
                    CompeletedTime[patient]=ActualServTime[patient]+CompeletedTime[patient-1]
        PatientTime[i]=np.sum(P_WaitingTime)
        DoctorTime[i]=np.sum(D_WaitingTime) 
         
    return (np.mean(PatientTime),np.mean(DoctorTime)) 


parameter=(16,3/4)
N=30     
AvgPatientWait,AvgDrWait = Simulation(N, parameter)
print("Average Waiting Times of all Patients: ",AvgPatientWait)

print("Average Time the practitioner is idle: ",AvgDrWait)

"""
3.46523971263
389.510718437

"""
        
        
        
        
    
    
    
    
