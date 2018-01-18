import matplotlib.pyplot as plt
import numpy as np

def problem2():

	process = []
	turnaroundTime = []
	x=0
	timeCounter = 0
	averageTurnaroundTime = 0
	result =[]

	n = input('請輸入Proces Number:')
	m = input('請輸入Max Quantum:')

	n=int(float(n))
	m=int(float(m))

	for i in range (0,n):
		process.append(i+1)
		turnaroundTime.append(0)

	for q in range(1,m+1):
		while process[x]!=0:			
			for i in range(0,n):
				if process[i]!=0:
					if (process[i] - q)>0:
						process[i] = process[i] - q
						timeCounter = timeCounter + q
					else:
						timeCounter = timeCounter + process[i]
						process[i] = 0
						turnaroundTime [i] = timeCounter

			while process[x]==0 and x < n-1:
				x = x + 1
		
		for i in range (0,n):
			averageTurnaroundTime = averageTurnaroundTime + turnaroundTime[i]
		
		averageTurnaroundTime = averageTurnaroundTime / n
		print('Quantum = ' + repr(q) + ' averageTurnaroundTime is ' + repr(averageTurnaroundTime) )

		result.append(averageTurnaroundTime)



		for i in range (0,n):
			process[i] = i+1
			turnaroundTime[i] = 0

		averageTurnaroundTime = 0;
		timeCounter = 0


	x = np.arange(1,m+1)

	plt.title("Problem2")
	plt.xlabel("Quantum")
	plt.ylabel("Average Turnaround Time") 

	plt.plot(x,result)

	plt.show()



problem2()





