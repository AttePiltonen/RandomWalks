import numpy as np
import matplotlib.pyplot as plt
import random
# %matplotlib inline
import matplotlib.cm as cm

walkers = 100 # choose the number of "walkers"
steps = 1000  # and the number of steps they will take

x = np.zeros(walkers)
y=np.zeros(walkers)

#   the random walk
for i in range(steps):
    for k in range(len(x)):
        # moves the position of the walker forwards or backwards
        x[k] = x[k] + random.choice([-1.,1.]) 

#    We want to represent the endpoints using circles with their 
#    size proportional to the distance from the origin
s = [0.5*abs(a) for a in x]  # distance from origin of each point
s = [a / max(s) for a in s]  # scales the sizes for visual clarity

# create colormap based on size
colors = [cm.winter(color) for color in s]  

# create a new figure
plt.figure()
ax = plt.gca()

# plot the circles to indicate distance from origin
for a, color, size in zip(x, colors, s):
    # plots circles using the colormap
    circle = plt.Circle((a, 0), size, color=color, fill=False)
    ax.add_artist(circle)

# limits for the x axis to ensure all points are visible
minx = 1.2*min(x)
maxx = 1.2*max(x)
plt.xlim([minx, maxx])
plt.ylim([-2,2])

# prints the end positions after the random walks
print(x)

plt.grid()
plt.show()



