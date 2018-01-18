import matplotlib.pyplot as plt
import numpy as np

cpuBurst = []
result = 0.0
guess = []
guess.append(10)
s = 0.0

print ('請輸入7個 CPU Burst Time')

for i in range(0,7):
	s = input()
	s=int(float(s))
	cpuBurst.append(s)
	result =  cpuBurst[i]/2 + guess[i]/2
	guess.append(result)

for i in range(0,7):
	print('When time = ' + repr(i) + ' the guess is ' + repr(guess[i]))

print('When time = ' + repr(7) + 'the guess is ' + repr(guess[7]))

plt.title("Problem4")
plt.xlabel("Time")
plt.ylabel("Guess(blue) vs Cpu Burst Time(green)") 

x = np.arange(0,8);
x1 = np.arange(0,7);

plt.plot(x,guess,x1,cpuBurst,'g')

plt.show()