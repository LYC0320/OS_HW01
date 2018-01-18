import matplotlib.pyplot as plt
import numpy as np

process = np.array([6, 3, 1,7])
turnaroundTime = np.array([0,0,0,0])
averageTurnaroundTime = 0;
timeCounter = 0
result = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0])

for q in range(1,8):
	while process[0]!=0 or process[1]!=0 or process[2]!=0 or process[3]!=0:			
		for i in range(0,4):
			if process[i]!=0:
				if (process[i] - q)>0:
					process[i] = process[i] - q
					timeCounter = timeCounter + q
				else:
					timeCounter = timeCounter + process[i]
					process[i] = 0
					turnaroundTime [i] = timeCounter
	averageTurnaroundTime = (turnaroundTime[0] + turnaroundTime[1] + turnaroundTime[2] + turnaroundTime[3]) /4
	

	result[q-1] = averageTurnaroundTime


	print (result[q-1])

	process = np.array([6, 3, 1,7])
	turnaroundTime = np.array([0,0,0,0])
	averageTurnaroundTime = 0;
	timeCounter = 0

x = np.arange(1,8);

plt.title("Problem1")
plt.xlabel("Quantum")
plt.ylabel("Average Turnaround Time") 

plt.plot(x,result)

plt.show()