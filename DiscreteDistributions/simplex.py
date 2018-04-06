import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

xs = []
ys = []
zs = []
colors = []
max = 8
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for m in range(11, 12):
    for x in range(0, m+1):
        for y in range(0, m - x + 1):
            z = m - (x + y)
            xs.append(x)
            ys.append(y)
            zs.append(z)
            if y < max and z < max:
                colors.append('red')
            else:
                colors.append('blue')
    ax.view_init(30, 10)
    ax.scatter(xs, ys, zs, color=colors)

plt.show()