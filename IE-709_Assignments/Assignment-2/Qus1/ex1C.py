import numpy as np
import matplotlib.pyplot as plt


def ServiceArea():
    l,w,k,N=20, 12, 50, 4    
    pixelsizeX,pixelsizeY=(l/k,w/k)
    # total pixel K*K
    NearL1=[]
    NearL2=[]
    NearL3=[]
    NearL4=[]
    X=np.arange(0,20.1,.4)
    Y=np.arange(0,12.2,0.24)
    points=[]
    for i in X:
        for j in Y:
            points.append((i,j))
    AP=np.array(points)
    A=np.transpose(AP)
    distL1=[]
    distL2=[]
    distL3=[]
    distL4=[]

    for i in range(len(AP)):
        M=[]
        for j in range(4):
            M.append((abs(AP[i][0]-Locations[j][0]) + abs(AP[i][1]-Locations[j][1])))
        k = min(M)
        if M.index(k)==0:
           NearL1.append(points[i])
           distL1.append(k)

        elif M.index(k)==1:
            NearL2.append(points[i])
            distL2.append(k)
        elif M.index(k)==2:
            NearL3.append(points[i])
            distL3.append(k)
        elif M.index(k)==3:
            NearL4.append(points[i])
            distL4.append(k)
    CoverPoints=np.array([len(NearL1),len(NearL2),len(NearL3),len(NearL4)])
    # make X and Y separate through tranpose
    NearL1=np.transpose(np.array(NearL1)) 
    NearL2=np.transpose(np.array(NearL2))
    NearL3=np.transpose(np.array(NearL3))
    NearL4=np.transpose(np.array(NearL4))
    #plotting
    plt.scatter(NearL1[0],NearL1[1])
    plt.scatter(NearL2[0],NearL2[1])
    plt.scatter(NearL3[0],NearL3[1])
    plt.scatter(NearL4[0],NearL4[1])
    plt.scatter(x=[6,8,14,12],y=[4,10,8,2],color='yellow')
    plt.savefig("ModifiedServiceLocations.png")
    plt.close()

    return (np.mean(distL1),np.mean(distL2),np.mean(distL3),np.mean(distL4),CoverPoints)
    

def PerformMeasure(S,PD):
    """ S= speed of travel(M/sec) PD = population density(per Node)"""
    AvgL1,AvgL2,AvgL3,AvgL4,CoverArea=ServiceArea()
    
    # Assume length an d width km
    TimeToService = [(AvgL1*1000)/(S*60),(AvgL2*1000)/(S*60),(AvgL3*1000)/(S*60),(AvgL4*1000)/(S*60)]

    print("For Speed of Travel 10 m/s and distance in Km")
    print("average time to service a call for the whole region(In Minutes): ",np.mean(TimeToService))   
    CoverArea=CoverArea/2601
    for i in range(4):
        print("Population cover by location"+str(Locations[i])+": ",CoverArea[i])
Locations=np.array([(3,4),(8,10),(18,7),(12,2)])
S=10  
PD=10  
PerformMeasure(S, PD)

        
            
