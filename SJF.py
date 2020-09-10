# list of processes
processsList = [{"processId": 1,  "arrivalTime": 3, "BurstTime": 1},
                {"processId": 2,  "arrivalTime": 1, "BurstTime": 4},
                {"processId": 3,  "arrivalTime": 4, "BurstTime": 2},
                {"processId": 4,  "arrivalTime": 0, "BurstTime": 6},
                {"processId": 5,  "arrivalTime": 2, "BurstTime": 3},
                ]

gantChart=[]
completedExec=0
for x in processsList:
    if x['arrivalTime']==0:
        gantChart.append({"processId": x["processId"], "startExec":x
        ["arrivalTime"], "endExec":x["BurstTime"]})
        completedExec=x['BurstTime']

# sort According to the arrival of the process
def myFunc(e):
    return e['BurstTime']

processsList.sort(key=myFunc)
      
for x in range(0, len(processsList)):
    if processsList[x]['arrivalTime'] == 0:
        continue
    else:
        completedExec=completedExec+processsList[x]["BurstTime"]
        gantChart.append({"processId": processsList[x]["processId"], "startExec": completedExec-processsList[x]['BurstTime'], "endExec":completedExec})
        
print(gantChart)

z = 0
for x, y in zip(gantChart, processsList):
 gantChart[z]['turnAroundTime']=x['endExec']-y['arrivalTime']
 gantChart[z]['waitingTime']=x['turnAroundTime']-y['BurstTime']
 z=z+1


print('Pid | startedExecutionOn |  CompletedExecutionOn\t|turnAroundTime |  waitingTIme ')
print('----------------------------------------------------------------------------------')
for x in gantChart:
    print(
        f"{x['processId']}  |\t\t{x['startExec']} \t |\t\t{x['endExec']}\t\t|\t{x['turnAroundTime']}      | {x['waitingTime']} ")

totalTurnAroundTime=0
totalWaitingTime=0
for x in gantChart:
    totalTurnAroundTime=totalTurnAroundTime+x['turnAroundTime']
    totalWaitingTime=totalWaitingTime+x['waitingTime']
print(f' The Average TurnAroundTime is {totalTurnAroundTime/len(gantChart)}')  
print(f'The Average Waiting Time is {totalWaitingTime/len(gantChart)}') 
