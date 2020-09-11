

def test(p):
    print(p)


def firstProcess(processList,gantChart):
    for x in processList:
        if x['arrivalTime']==0:
            gantChart=[{"processId":x['processId'],"startExec":x['arrivalTime'],"endExec":x['BurstTime'],"turnAroundTime":x['BurstTime'],"waitingTime":0}]
    return [processList,gantChart]


def SchedulingAlgo(processList,gantChart):
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


