import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

# a large number is needed here to show the statistical behaviour of random wal$
walkers = 10000000

x = np.zeros(walkers)

# set up the plot
fig1 = plt.figure()
sns.set_style("ticks")
plt.grid()
axes = plt.gca()
axes.set_xlabel('End position')
axes.set_ylabel('Number of walkers')

# random walk with a variable number of steps
def endpos(s):
    p = np.zeros(walkers)
    for i in range(walkers):
        for k in range(s):
            p[i] += random.choice([-1,1])
    return p

# calculate the endpoints of the walkers for the desire number of steps
x = endpos(45)

# some statistical parameters
meanpos = np.mean(x) # the mean will be ≈ 0
stdevpos = np.std(x) # the standard deviation ≈ the square root of the number o$
print(meanpos)
print(stdevpos)

# plot histogram with a suitable number of bins to see the population at each s$
plt.hist(x,int(max(x)),ec='k')
sns.despine()
plt.show()


# we can also plot the mean squared endpoint distance to see it is equal to the$
fig2 = plt.figure()
sns.set_style("ticks")
plt.grid()
axes = plt.gca()
axes.set_xlabel('Number of steps')
axes.set_ylabel('Mean squared endpoint distance')

#ydata = [np.mean(endpos(5)**2),np.mean(endpos(10)**2),np.mean(endpos(15)**2),n$
#xdata = [5,10,15,64]

#plt.plot(xdata,ydata)
