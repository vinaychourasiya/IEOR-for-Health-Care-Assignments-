import numpy as np

def Simulation(N,parameter):
    alpha,theta=parameter
    PatientTime=np.zeros(10000)
    DoctorTime=np.zeros(10000)
    for i in range(10000):
    
        D_WaitingTime=np.zeros(N)
        P_WaitingTime=np.zeros(N)
        
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
        #print(P_WaitingTime)
        #print(D_WaitingTime)
        PatientTime[i]=np.sum(P_WaitingTime)
        DoctorTime[i]=np.sum(D_WaitingTime)
    #print(PatientTime)
    #print(DoctorTime)     
    return (np.mean(PatientTime),np.mean(DoctorTime)) 


parameter=(16,3/4)
N=30
ScheduledTime=[0,5,18,29,42,53,66,77,90,101,114,125,138,149,162,173,186,197,210,221,234,245,258,269,282,293,306,317,330,341]
AvgPatientWait,AvgDrWait = Simulation(N, parameter)
print("Shchedule time suggeted: ",ScheduledTime )
print("Average Waiting Times of all Patients: ",AvgPatientWait)

print("Average Time the practitioner is idle: ",AvgDrWait)

   
        
        
        
    
    
    
    
