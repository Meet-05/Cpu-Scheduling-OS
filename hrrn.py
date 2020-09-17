
# # Sample input
processList = [{"processId": 0,  "arrivalTime": 0, "BurstTime": 3},
               {"processId": 1,  "arrivalTime": 2, "BurstTime": 6},
               {"processId": 2,  "arrivalTime": 4, "BurstTime": 4},
               {"processId": 3,  "arrivalTime": 6, "BurstTime": 5},
               {"processId": 4,  "arrivalTime": 8, "BurstTime": 2}, ]


arrivedProcesses=[]
tempArrived=[]
gantChart=[]

#rr=(waitingTime+burstTime)/BUrstTime    rr grt that will be served first      

def findArrivedProcesses(x):
    global currentTimeStamp
    for y in range(x,len(processList)):
                if processList[y]['arrivalTime']<currentTimeStamp:
                    arrivedProcesses.append(processList[y])
                    tempArrived.append(processList[y]) 
                    # currentTimeStamp=currentTimeStamp+processList[y]['BurstTime']        
                    # print(tempArrived)
    
def calculateHrr():
    currentTime=gantChart[len(gantChart)-1]['endExec'] 
    rrTime=[]
    for process in tempArrived: 
        waitingTime=currentTime-process['arrivalTime']
        BurstTime=process['BurstTime']
        rr=(waitingTime+BurstTime)/BurstTime
        rrTime.append(rr)
    maxPos=rrTime.index(max(rrTime))
    nextProcess=tempArrived[maxPos]
    # print(f'next process is {nextProcess}')
    del tempArrived[maxPos]
    return nextProcess
    # print(f'after deleting {tempArrived}')

def insertInGant(process):
    processId=process['processId']
    startExec=gantChart[len(gantChart)-1]['endExec'] 
    arrivalTime=process['arrivalTime']
    BurstTime=process['BurstTime']
    endExec=startExec+BurstTime
    gantChart.append({'processId':processId ,'startExec':startExec,'endExec':endExec})

for x in range(len(processList)):
    global currentTimeStamp
    if processList[x]['arrivalTime']==0:
        arrivedProcesses.append(processList[x])
        currentTimeStamp=processList[x]['BurstTime']
        startExec=processList[x]['arrivalTime']
        endExec=processList[x]['BurstTime']
        gantChart.append({'proccessId':processList[x]['processId'],'startExec':startExec,'endExec':endExec,'turnAroundTime':endExec,'waitingTime':0})
 
    elif processList[x]['arrivalTime']<currentTimeStamp:
            #this function will return a list of process arrived at the currentTimeStamp
            findArrivedProcesses(x)
            print(tempArrived) 
            # at this point i get all the arrived processes in current TimeStamp
            if  len(tempArrived)==1:
                processId=tempArrived[0]['processId']
                arrivalTime=tempArrived[0]['arrivalTime']
                BurstTime=tempArrived[0]['BurstTime']
                startExec=gantChart[len(gantChart)-1]['endExec']
                endExec=startExec+BurstTime
                gantChart.append({'processId':processId,'arrivalTime':arrivalTime,'BurstTime':BurstTime,'startExec':startExec,'endExec':endExec})
            
            if len(tempArrived)>1:
                count=len(tempArrived)
                print('More processes arrived Now calculate response Ratio of those processes')  
                nextProcess=calculateHrr()    
                print(f'next process is {nextProcess}')
                insertInGant(nextProcess)
                print(f'after deleting {tempArrived}')
            # print(arrivedProcesses)
            currentTimeStamp=currentTimeStamp+arrivedProcesses[len(arrivedProcesses)-1]['BurstTime']
            tempArrived=[]
            print('-----------------------------------------------------------------------')
            if len(arrivedProcesses)==len(processList):
                break        
          

print(f'gantChart is ----->{gantChart}')


    
# for  y in arrivedProcesses:
#          print(f'---------{y}')

currentTimeStamp=0

