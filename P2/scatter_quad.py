import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    data = np.loadtxt('3dpd.out', delimiter=',')
    x = data[:,0]
    y = data[:,1]
    z = data[:,2]
    a = 1
    b = 0.4
    c = -2.4
    xr = data[np.where(a*data[:, 2] + b*(np.square(data[:, 1]) + np.square(data[:, 0])) + c >= 0)]
    ax.scatter(xr[:, 0], xr[:, 1], xr[:, 2], c='b', marker='o')
    xb = data[np.where(a*data[:, 2] + b*(np.square(data[:, 1]) + np.square(data[:, 0])) + c < 0)]
    ax.scatter(xb[:, 0], xb[:, 1], xb[:, 2], c='r', marker='o')
    plt.show()