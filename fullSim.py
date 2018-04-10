import os
import time

goodInput = True

simType = input("Welcome to the multicore scratchpad and cache simulator!\nPlease choose an option for memory simulation by entering the corresponding number \n1.Hash\n2.Heap\n3.Stride\n4.Trace\n")
if int(simType) == 1:
    print("Now running a hash benchmark")
    os.system("fullSim.bat hash")
elif int(simType) == 2:
    print("Now running a heap benchmark")
    os.system("fullSim.bat heap")
elif int(simType) == 3:
    print("Now running a stride benchmark")
    os.system("fullSim.bat stride")
elif int(simType) == 4:
    print("Now running a trace benchmark")
    os.system("fullSim.bat 4")
else:
    print("You did not chose an appropriate number. Please try 1, 2, 3, or 4\n")
    goodInput = False

time.sleep(5)

if goodInput:
    print("Scratch pad memory results:")
    f = open('spmLog.txt','r')
    print(f.read())
    f.close()

    print("Cache memory results:")
    f = open('cacheLog.txt','r')
    print (f.read())
    f.close()







