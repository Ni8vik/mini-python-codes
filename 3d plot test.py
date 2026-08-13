import matplotlib.pyplot as plt
import numpy as np


# Create data
x = np.linspace(-3, 3, 40)
y = np.linspace(-3, 3, 60)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2)) + 0.3 * X * Y  # Gaussian peak + saddle

# Create figure with 3 subplots
fig = plt.figure(figsize=(15, 5))

# 1. WIREFRAME PLOT
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_wireframe(X, Y, Z, color='blue', linewidth=0.5)
ax1.set_title('Wireframe Plot\n(skeleton of surface)')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# 2. CONTOUR PLOT (projected on bottom plane)
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(X, Y, Z, alpha=0.3, cmap='viridis')  # semi-transparent surface
ax2.contour(X, Y, Z, zdir='z', offset=Z.min() - 0.2, cmap='cool', levels=15)
ax2.set_title('3D Contour Plot\n(lines projected on bottom)')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

# 3. QUIVER PLOT (vector field)
ax3 = fig.add_subplot(133, projection='3d')
# Calculate gradient (vectors point uphill)
U, V = np.gradient(Z)  # slope in X and Y directions
W = np.zeros_like(U)   # no vertical component for clarity
# Plot every 3rd point to avoid crowding
step = 3
ax3.quiver(X[::step, ::step], Y[::step, ::step], Z[::step, ::step],
           U[::step, ::step], V[::step, ::step], W[::step, ::step],
           length=0.3, color='red', normalize=True)
ax3.set_title('Quiver Plot\n(vector field / gradient)')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')

plt.tight_layout()
plt.show()