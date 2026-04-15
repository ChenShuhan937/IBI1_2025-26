#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt 
#define the basic variables of the model, one for each of the population
N=10000 #total number of people
S=N-1 #the number of susceptible people 
I=1 #the initial infected number
R=0 #the initial recovered number

beta=0.3 
gamma=0.05
#record history
S_history=[S]
I_history=[I]
R_history=[R]
#Code the time loop (loop over 1000 times)
for t in range(1000):
    #The possibility for random healthy individual to get infected= beta*the propotion of infected
    new_infected = np.random.choice([0,1], size=S, p=[1-beta*(I/N), beta*(I/N)] ).sum()
    #The possibility for random infected individual to get recovered=gamma
    new_recovered = np.random.choice([0,1], size=I, p=[1-gamma, gamma]).sum()
    #Update the number
    S -= new_infected
    I += new_infected-new_recovered
    R += new_recovered
    #record the changes in number after each loop
    S_history.append(S)
    I_history.append(I)
    R_history.append(R)
#Draw the figure
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_history, label='Susceptible',color='blue')
plt.plot(I_history, label='Infected',color='red')
plt.plot(R_history, label='Recovered',color='green')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('Stochastic SIR Model')
plt.legend()
#Save the plot
plt . savefig ("SIR_plot.png", format="png")
#Show the plot
plt.show()