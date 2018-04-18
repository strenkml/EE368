import os
import time

keepSimulating = True

while keepSimulating:
		
	goodInput = True
	simType = input("Welcome to the multicore scratchpad and cache simulator!\nPlease choose an option for memory simulation by entering the corresponding number \n1.Hash\n2.Heap\n3.Stride\n4.Trace\n5.Exit simulator\n")
	
	if not os.path.exists('..\\Results'):
		os.makedirs('..\\Results')
	
	try:
		if int(simType) == 1:
			os.system("fullSim.bat hash")
		elif int(simType) == 2:
			os.system("fullSim.bat heap")
		elif int(simType) == 3:
			os.system("fullSim.bat stride")
		elif int(simType) == 4:
			os.system("fullSim.bat 4")
		elif int(simType) == 5:
			keepSimulating = False	
		else:
			print("You did not chose an appropriate number. Please try 1, 2, 3, 4, or 5\n")
			goodInput = False
			
		time.sleep(5)
	except:
		print("You did not chose an appropriate number. Please try 1, 2, 3, 4, or 5\n")
		goodInput = False

	if goodInput and keepSimulating:
	
		print("Scratch pad memory results:")
		tempF = open('..\\Results\\tempSpmLog.txt','r')
		f = open('..\\Results\\spmLog.txt','w')
		for line in tempF.readlines():
			if "Cost:" not in line and "1:" not in line:
				print(line.rstrip())
				f.write(line)
		tempF.close()
		f.close()
		os.remove('..\\Results\\tempSpmLog.txt')
		
		print("\n")
		
		print("Cache memory results:")
		tempF = open('..\\Results\\tempCacheLog.txt','r')
		f = open('..\\Results\\cacheLog.txt','w')
		for line in tempF.readlines():
			if "Cost:" not in line and "1:" not in line:
				print(line.rstrip())
				f.write(line)
		tempF.close()
		f.close()
		os.remove('..\\Results\\tempCacheLog.txt')
		print("\n\n\n")







