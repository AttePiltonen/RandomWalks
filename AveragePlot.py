# Creates a plot of multiple random walkers and their position at each step
# and plots the average position all on the same graph

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

walkers = 10
start = 0
steps = 10000

askel_lista = np.empty(shape=(walkers, steps + 1))

# the random walk algorithm
for i in range(walkers):
        # create an array of random steps
        askeleet = np.random.choice([-1,1], steps)
        # initalize an array to store the positions of the walker
        lista = np.zeros(steps + 1)
        lista[0] = start
        lista[1:] = np.cumsum(askeleet)
        plt.plot(lista, color = 'grey')
        # store the steps
        askel_lista[i,:] = lista

sns.set_style('ticks')
plt.grid()
axes = plt.gca()
axes.set_xlim([0,steps])
axes.set_xlabel('Step')
axes.set_ylabel('Position')

# plot the average of all the walkers
plt.plot(np.mean(askel_lista, axis=0), color="red")
sns.despine()
plt.show()
