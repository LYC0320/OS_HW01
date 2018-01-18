import matplotlib.pyplot as plt
import numpy as np

cpuBurst = np.array([6,4,6,4,13,13,13])
result = 0.0;
guess = []


guess.append(10)

for i in range(0,7):
	result = cpuBurst[i]/2 + guess[i]/2
	guess.append(result)
	print('When time = ' + repr(i) + ' the guess is ' + repr(guess[i]))

print('When time = ' + repr(7) + 'the guess is ' + repr(guess[7]))
#print('When time = ' + repr(8) + 'the guess is ' + repr(guess[8]))

plt.title("Problem3")
plt.xlabel("Time")
plt.ylabel("Guess(blue) vs Cpu Burst Time(green)") 

x = np.arange(0,8);
x1 = np.arange(0,7);

plt.plot(x,guess,x1,cpuBurst,'g')

plt.show()

