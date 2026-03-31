#Practical4.5
#Initial conditions
total_population=1000
infected=1
susceptible=total_population-infected
infection_rate=0.002
recovery_rate=0.1
days=100
#keep the daily infected number in histogram
infected_history=[infected]
for day in range(1, days):
    #calculate the number of new infected people
    new_infected=infection_rate*susceptible*infected/total_population
    #calculate the number of new recovery
    new_recovered=recovery_rate*infected
    #update the data
    infected+=new_infected-new_recovered
    susceptible-=new_infected
    #keep current infection number in record
    infected_history.append(infected)
#print the data for the first five days to check if the code is correct   
print("Day | Infected")
for i in range (5):
    print(f"{i+1} | {infected_history[i]:.2f}")
    

    
