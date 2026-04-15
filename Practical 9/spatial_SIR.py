# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Make array of all susceptible population. 100x100 grid: 0=Susceptible, 1=Infected, 2=Recovered
population = np.zeros((100, 100))
# Random initial infection site
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# Model parameters
beta = 0.3
gamma = 0.05
# 8-directional neighbors for spatial spread
dirs = [(-1,-1),(-1,0),(-1,1),
        (0,-1),        (0,1),
        (1,-1),(1,0),(1,1)]

# Spatial SIR simulation
# 1. Locate all infected people in the grid
# 2. For each infected person, attempt to infect 8 neighbors
# 3. Infected person recovers stochastically
# 4. Update grid states
# 5. Plot grid every 10 steps
for step in range(100):
    new_infect = []
    new_recover = []
    # Find coordinates of all infected people
    inf_x, inf_y = np.where(population == 1)
    
    for x, y in zip(inf_x, inf_y):
        # Spread infection to neighbors
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 100 and 0 <= ny < 100:
                if population[nx, ny] == 0:
                    if np.random.rand() < beta:
                        new_infect.append((nx, ny))
        # Stochastic recovery for infected people
        if np.random.rand() < gamma:
            new_recover.append((x, y))
    
    # Update infected and recovered states
    for x, y in new_infect:
        population[x, y] = 1
    for x, y in new_recover:
        population[x, y] = 2
    
    # Plot grid every 10 time steps
    if step % 10 == 0:
        plt.figure(figsize=(6,4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time step {step}')
        plt.show()