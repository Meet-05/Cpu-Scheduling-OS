from CpuScheduler import SchedulingAlgo,printOutput,firstProcess

# list of processes
processList = [{"processId": 1,  "arrivalTime": 0, "BurstTime": 2},
                {"processId": 2,  "arrivalTime": 1, "BurstTime": 2},
                {"processId": 3,  "arrivalTime": 5, "BurstTime": 3},
                {"processId": 4,  "arrivalTime": 6, "BurstTime": 4},
                ]
gantChart=[]
result=firstProcess(processList,gantChart)
processList=result[0]
gantChart=result[1]

def myFunc(e):
    return e['arrivalTime']   
processList.sort(key=myFunc)










SchedulingAlgo(processList,gantChart)
printOutput(gantChart, processList)






#------------------------------------
#
# def SJF(processList,gantChart):
#     z=1
#     for x in range (0,len(processList)):
#                 if(processList[x]['arrivalTime'])==0:
#                     continue
#                 else:
#                     prevEndExec=gantChart[x-1]['endExec']
#                     if(processList[x]['arrivalTime']>int(prevEndExec)):
#                         startExec=processList[x]['arrivalTime']
#                         endExec=startExec+processList[x]['BurstTime']
#                         turnAroundTime=endExec-processList[x]['arrivalTime']
#                         waitingTime=turnAroundTime-processList[x]['BurstTime']
#                         gantChart.append({"processId":processList[x]['processId'],"startExec":startExec,"endExec":endExec,"turnAroundTime":turnAroundTime,"waitingTime":waitingTime})
#                         # print("-----------------------------------------------")
#                         z=z+1
#                     else:
#                         startExec=gantChart[z-1]['endExec']
#                         endExec=startExec+processList[x]['BurstTime']
#                         turnAroundTime=endExec-processList[x]['arrivalTime']
#                         waitingTime=turnAroundTime-processList[x]['BurstTime']
#                         gantChart.append({"processId":processList[x]['processId'],"startExec":startExec,"endExec":endExec,"turnAroundTime":turnAroundTime,"waitingTime":waitingTime})
#                         z=z+1

 
# def printOutput(gantChart, processList):
#     # Turn around Time is : ExitTime-Arrival Time
#     # waiting time is :TurnAroundTime-BurstTime
   
#     print('Pid | startedExecutionOn |  CompletedExecutionOn\t|turnAroundTime |  waitingTIme ')
#     print('----------------------------------------------------------------------------------')
#     for x in gantChart:
#         print(
#             f"{x['processId']}  |\t\t{x['startExec']} \t |\t\t{x['endExec']}\t\t|\t{x['turnAroundTime']}      | {x['waitingTime']} ")

#     totalTurnAroundTime = 0
#     totalWaitingTime = 0
#     for x in gantChart:
#         totalTurnAroundTime = totalTurnAroundTime+x['turnAroundTime']
#         totalWaitingTime = totalWaitingTime+x['waitingTime']
#     print(
#         f' The Average TurnAroundTime is {totalTurnAroundTime/len(gantChart)}')
#     print(f'The Average Waiting Time is {totalWaitingTime/len(gantChart)}')





