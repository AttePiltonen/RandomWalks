import numpy as np
import matplotlib.pyplot as plt
import random
#%matplotlib inline
import matplotlib.cm as cm

# Random walk radially, evenly spaced points moving radially about the origin

steps = 901

def circle_points(r, n):
    circles = []
    t = np.linspace(0, 2*np.pi, n, endpoint=False) # spaces points evenly
    xc=np.zeros(n)
    yc=np.zeros(n)
    for k in range(n):
        xc[k] = r[k] * np.cos(t[k]) # points lay along a circle
        yc[k] = r[k] * np.sin(t[k])
    for i in range(steps):
        for k in range(n):
            r[k] = r[k] + random.choice([-10.2,15.]) # random radial walk
            xc[k] = r[k] * np.cos(t[k]) # new point 
            yc[k] = r[k] * np.sin(t[k])
    
    circles.append(np.c_[xc, yc])
    return circles

cwalkers = 9
# set initial radius
r = np.repeat(901.,cwalkers)

# call the random walk function
circles = circle_points(r, cwalkers)

# plot the points
fig, ax = plt.subplots()
for circle in circles:
    ax.scatter(circle[:, 0], circle[:, 1])
ax.set_aspect('equal')

# plot the average final radial distance for reference
avgr=np.average(abs(r))
circle1 =plt.Circle((0,0), radius=avgr, color='m', fill=False)

# print the average radial distance and the endpoints
print(avgr)
print(r)

plt.gca().add_patch(circle1)

# set limits to ensure visibility and display plot
plt.xlim([-1.2*max(abs(r)),1.2*max(abs(r))])
plt.ylim([-1.2*max(abs(r)),1.2*max(abs(r))])
plt.grid()
plt.show()





