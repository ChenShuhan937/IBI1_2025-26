#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt 
#vaccine rates (0~100%)
vacc_rates= [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
#define the basic variables of the model, one for each of the population
N=10000
beta=0.3
gamma=0.05

plt.figure(figsize=(6,4), dpi=150)

for r in vacc_rates:

    I = 1
    R = 0
    V = int(N*r)
    S = max(N - V - 1, 0)
#record history
    I_history=[I]


#Code the time loop (loop over 1000 times)
    for t in range(1000):
    #The possibility for random healthy individual to get infected= beta*the propotion of infected
        if S > 0:
            new_infected = np.random.choice([0,1], size=S, p=[1-beta*(I/N), beta*(I/N)]).sum()
        else:
            new_infected = 0
    #The possibility for random infected individual to get recovered=gamma
        if I > 0:
            new_recovered = np.random.choice([0,1], size=I, p=[1-gamma, gamma]).sum()
        else: 
            new_recovered = 0
    #Update the number
        S -= new_infected
        I += new_infected-new_recovered
        R += new_recovered
    
        I_history.append(I)

    #Draw the figure
    plt.plot(I_history, label=f'{int(r*100)}% vaccinated')

plt.xlabel('Time')
plt.ylabel('Infected people')
plt.title('Effect of Vaccination')
plt.legend()
#Save the plot
plt.savefig ("SIR_vaccination_plot.png", format="png")
#Show the plot
plt.show()