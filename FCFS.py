# list of processes
# processsList = [{"processId": 0,  "arrivalTime": 2, "BurstTime": 4},
#                 {"processId": 1,  "arrivalTime": 1, "BurstTime": 2},
#                 {"processId": 2,  "arrivalTime": 0, "BurstTime": 3},
#                 {"processId": 3,  "arrivalTime": 4, "BurstTime": 2},
#                 {"processId": 4,  "arrivalTime": 3, "BurstTime": 1},
#                 ]

# sort According to the arrival of the process


def myFunc(e):
    return e['arrivalTime']


def check(processsList, gantChart, x):
    if processsList[x]["arrivalTime"] > gantChart[x-1]["endExec"]:
        print(f"---------------{processsList[x]['arrivalTime']}")
        return processsList[x]["arrivalTime"]
    else:
        return gantChart[x-1]["endExec"]


def fcfs(processsList):
    processsList.sort(key=myFunc)
    # prepare the gant chart
    completedExec = processsList[0]['BurstTime']
    gantChart = []
    for x in range(0, len(processsList)):
        if processsList[x]['arrivalTime'] == 0:
            gantChart.append({"processId": processsList[x]['processId'],  "startExec": processsList[0]
                              ["arrivalTime"], "endExec": processsList[0]["BurstTime"], "turnAroundTime": 0, "watingTime": 0})
        else:
            # completedExec = completedExec+processsList[x]['BurstTime']
             start=check(processsList,gantChart,x)
             endTime=start+processsList[x]['BurstTime']
             gantChart.append({"processId": processsList[x]['processId'],  "startExec": check(
                processsList, gantChart, x), "endExec":endTime, "turnAroundTime": 0, "watingTime": 0})

    return gantChart




def printOutput(gantChart, processList):
    # Turn around Time is : ExitTime-Arrival Time
    # waiting time is :TurnAroundTime-BurstTime
    z = 0
    for x, y in zip(gantChart, processList):
        gantChart[z]['turnAroundTime'] = x['endExec']-y['arrivalTime']
        gantChart[z]['waitingTime'] = x['turnAroundTime']-y['BurstTime']
        z = z+1
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


# --static Execution-------------
# gantChart=fcfs(processsList)
# printOutput(gantChart,processsList)


# ----------static (userInput------------
dummyProcessList = []
s = int(input('Enter the number of processes'))


def processInput(dummyProcessList):
    processId = int(input("Enter the processId"))
    arrivalTime = int(input("Enter the ArrivalTime:"))
    burstTime = int(input("enter the BurstTime"))
    dummyProcessList.append(
        {"processId": processId, "arrivalTime": arrivalTime, "BurstTime": burstTime})


for x in range(0, s):
    processInput(dummyProcessList)


gantChart = fcfs(dummyProcessList)
printOutput(gantChart, dummyProcessList)


# ---dynamic-------------------------------
# print('to enter a new process type p ')
# print('to see the schedule press r')
# print('to quit press q')

# i=str
# while(True):
#     i=input('Enter your Choice')
#     if(i=='p'):
#         processInput(dummyProcessList)
#     if(i=='r'):
#            gantChart=fcfs(dummyProcessList)
#            printOutput(gantChart,dummyProcessList)
#     if(i=='q'):
#         exit()
