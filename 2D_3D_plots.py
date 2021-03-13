import numpy as np
import matplotlib.pyplot as plt

# Simulates random walks in two and three dimensions and plots them

stepsize = 2
steps = 1000

# take a step in a random direction in x and y
kulmat = (np.random.uniform(0,2*np.pi,steps))
xaskeleet = np.cumsum(stepsize * np.cos(kulmat))
yaskeleet = np.cumsum(stepsize * np.sin(kulmat))

fig1 = plt.figure()
plt.grid()

# random walk in the z direction
zaxis = np.random.uniform(-1,1,steps)
z = np.cumsum(zaxis)

# plot the random walk in two dimensions
plt.plot(xaskeleet,yaskeleet)
plt.show()

# now plot the third dimension as well
fig2 = plt.figure()
ax = fig2.add_subplot(projection="3d")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Random Walk')
ax.plot(xaskeleet,yaskeleet,z)

plt.show()


