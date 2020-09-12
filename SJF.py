from CpuScheduler import SchedulingAlgo,printOutput,firstProcess


gantChart=[]

# #----Sorting and scheduling first process arrived------------------
# result=firstProcess(processList,gantChart)
# processList=result[0]
# gantChart=result[1]
def myFunc(e):
    return e['BurstTime']   
# processList.sort(key=myFunc)

# #------------------FCFS Scheduling and print output------
# SchedulingAlgo(processList,gantChart)
# printOutput(gantChart, processList)

processList=[]


def sjf(processList,gantChart): 
    result=firstProcess(processList,gantChart)
    processList=result[0]
    gantChart=result[1]
    processList.sort(key=myFunc)
    SchedulingAlgo(processList,gantChart)
    printOutput(gantChart, processList)

def createProcess(count):
    for x in range(count):
        processId=int(input('enter the processId: '))
        arrivalTime=int(input('enter the arrivalTime:'))
        burstTime=int(input('enter the BurstTime:'))
        processList.append({"processId":processId,"arrivalTime":arrivalTime,"BurstTime":burstTime})
        sjf(processList,gantChart)

  
while(True):
    stop=input('enter q to quit, c to enter Processes ')
    if(stop!='q'):
        count=int(input('Enter the number of Processes'))
        createProcess(count)
    else:
        exit() 
#------------------ Sample input----------
# processList = [{"processId": 1,  "arrivalTime": 3, "BurstTime": 1},
#                 {"processId": 2,  "arrivalTime": 1, "BurstTime": 4},
#                 {"processId": 3,  "arrivalTime": 4, "BurstTime": 2},
#                 {"processId": 4,  "arrivalTime": 0, "BurstTime": 6},
#                 {"processId": 5,  "arrivalTime": 2, "BurstTime": 3},
#                 ]
