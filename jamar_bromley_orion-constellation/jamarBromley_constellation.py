# 1
#%matplotlib notebook
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 2
# Orion
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]

# 3
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x,y, marker = '*')
ax.set_title('2D Constellation View')
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
plt.show()

# 4
fig_3d = plt.figure()
ax = fig_3d.add_subplot(1,1,1, projection='3d')
constellation3d = ax.scatter(x,y,z, marker='*')
ax.set_title('Constellation of Orion', size=('small'), weight=('bold'))
ax.set_xlabel('X_Axis', size=('x-small'), weight=('bold'))
ax.set_ylabel('Y_Axis', size=('x-small'), weight=('bold'))
ax.set_zlabel('Z_Axis', size=('x-small'), weight=('bold'))

plt.show()

# 5
x2 = [22.4, 33.7, 18.4, 24.3]
y2 = [58.3, 55.2, 48.4, 44.4]
z2 = [18.5, 19.3, 26.6, 20.4]

some_stars = plt.figure()
ax = some_stars.add_subplot(1,1,1, projection='3d')
new_constellation3D = ax.scatter(x2,y2,z2, marker='*')
ax.set_title('Aldebaran, Bonner Stars, 39 Tauri', size=('small'), weight=('bold'))
ax.set_xlabel('Celestial X Coordinate', size=('x-small'), fontstyle=('italic'))
ax.set_ylabel('Celestial Y Coordinate', size=('x-small'), fontstyle=('italic'))
ax.set_zlabel('Celestial Z Coordinate', size=('x-small'), fontstyle=('italic'))

plt.show()
