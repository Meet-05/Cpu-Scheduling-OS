#[[1,2,2],[1,2,2],[4,5,5],[3,5,4]]
from CpuScheduler import SchedulingAlgo,printOutput,firstProcess




gantChart=[]

# #----Sorting and scheduling first process arrived------------------
# result=firstProcess(processList,gantChart)
# processList=result[0]
# gantChart=result[1]
def myFunc(e):
    return e['arrivalTime']   
# processList.sort(key=myFunc)

# #------------------FCFS Scheduling and print output------
# SchedulingAlgo(processList,gantChart)
# printOutput(gantChart, processList)

processList=[]


def fcfs(processList,gantChart): 
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
        fcfs(processList,gantChart)

  
while(True):
    stop=input('enter q to quit, c to continue ')
    if(stop!='q'):
        count=int(input('Enter the number of Processes'))
        createProcess(count)
    else:
        exit() 

  
    
    

    