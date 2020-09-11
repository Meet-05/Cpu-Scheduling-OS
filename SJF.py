# list of processes
processList = [{"processId": 1,  "arrivalTime": 3, "BurstTime": 1},
                {"processId": 2,  "arrivalTime": 1, "BurstTime": 4},
                {"processId": 3,  "arrivalTime": 4, "BurstTime": 2},
                {"processId": 4,  "arrivalTime": 0, "BurstTime": 6},
                {"processId": 5,  "arrivalTime": 2, "BurstTime": 3},
                ]

gantChart=[]
for x in processList:
    if x['arrivalTime']==0:
        gantChart=[{"processId":x['processId'],"startExec":x['arrivalTime'],"endExec":x['BurstTime'],"turnAroundTime":x['BurstTime'],"waitingTime":0}]

def myFunc(e):
    return e['BurstTime']
    
processList.sort(key=myFunc)

def SJF(processList,gantChart):
    z=1
    for x in range (0,len(processList)):
                if(processList[x]['arrivalTime'])==0:
                    continue
                else:
                    prevEndExec=gantChart[x-1]['endExec']
                    if(processList[x]['arrivalTime']>int(prevEndExec)):
                        startExec=processList[x]['arrivalTime']
                        endExec=startExec+processList[x]['BurstTime']
                        turnAroundTime=endExec-processList[x]['arrivalTime']
                        waitingTime=turnAroundTime-processList[x]['BurstTime']
                        gantChart.append({"processId":processList[x]['processId'],"startExec":startExec,"endExec":endExec,"turnAroundTime":turnAroundTime,"waitingTime":waitingTime})
                        print("-----------------------------------------------")
                        z=z+1
                    else:
                        startExec=gantChart[z-1]['endExec']
                        endExec=startExec+processList[x]['BurstTime']
                        turnAroundTime=endExec-processList[x]['arrivalTime']
                        waitingTime=turnAroundTime-processList[x]['BurstTime']
                        gantChart.append({"processId":processList[x]['processId'],"startExec":startExec,"endExec":endExec,"turnAroundTime":turnAroundTime,"waitingTime":waitingTime})
                        z=z+1

 
def printOutput(gantChart, processList):
    # Turn around Time is : ExitTime-Arrival Time
    # waiting time is :TurnAroundTime-BurstTime
   
    print('Pid | startedExecutionOn |  CompletedExecutionOn\t|turnAroundTime |  waitingTIme ')
    print('----------------------------------------------------------------------------------')
    for x in gantChart:
        print(
            f"{x['processId']}  |\t\t{x['startExec']} \t |\t\t{x['endExec']}\t\t|\t{x['turnAroundTime']}      | {x['waitingTime']} ")

    totalTurnAroundTime = 0
    totalWaitingTime = 0
    for x in gantChart:
        totalTurnAroundTime = totalTurnAroundTime+x['turnAroundTime']
        totalWaitingTime = totalWaitingTime+x['waitingTime']
    print(
        f' The Average TurnAroundTime is {totalTurnAroundTime/len(gantChart)}')
    print(f'The Average Waiting Time is {totalWaitingTime/len(gantChart)}')



SJF(processList,gantChart)
printOutput(gantChart, processList)





#--------------------------
# gantChart=[]
# completedExec=0
# for x in processsList:
#     if x['arrivalTime']==0:
#         gantChart.append({"processId": x["processId"], "startExec":x
#         ["arrivalTime"], "endExec":x["BurstTime"]})
#         completedExec=x['BurstTime']

# # sort According to the arrival of the process
# def myFunc(e):
#     return e['BurstTime']

# processsList.sort(key=myFunc)
      
# for x in range(0, len(processsList)):
#     if processsList[x]['arrivalTime'] == 0:
#         continue
#     else:
#         completedExec=completedExec+processsList[x]["BurstTime"]
#         gantChart.append({"processId": processsList[x]["processId"], "startExec": completedExec-processsList[x]['BurstTime'], "endExec":completedExec})
        
# print(gantChart)

# z = 0
# for x, y in zip(gantChart, processsList):
#  gantChart[z]['turnAroundTime']=x['endExec']-y['arrivalTime']
#  gantChart[z]['waitingTime']=x['turnAroundTime']-y['BurstTime']
#  z=z+1


# print('Pid | startedExecutionOn |  CompletedExecutionOn\t|turnAroundTime |  waitingTIme ')
# print('----------------------------------------------------------------------------------')
# for x in gantChart:
#     print(
#         f"{x['processId']}  |\t\t{x['startExec']} \t |\t\t{x['endExec']}\t\t|\t{x['turnAroundTime']}      | {x['waitingTime']} ")

# totalTurnAroundTime=0
# totalWaitingTime=0
# for x in gantChart:
#     totalTurnAroundTime=totalTurnAroundTime+x['turnAroundTime']
#     totalWaitingTime=totalWaitingTime+x['waitingTime']
# print(f' The Average TurnAroundTime is {totalTurnAroundTime/len(gantChart)}')  
# print(f'The Average Waiting Time is {totalWaitingTime/len(gantChart)}') 
