import numpy as np
import matplotlib.pyplot as plt

# Constants
mu = 398600  # Earth gravitational parameter

# Orbit radii (km)
r1 = 7000       # Low Earth Orbit
r2 = 384400     # Moon orbit distance

# Hohmann transfer calculations
a = (r1 + r2) / 2  # semi-major axis

# Velocity in initial orbit
v1 = np.sqrt(mu / r1)

# Velocity in transfer orbit at r1
v_transfer = np.sqrt(mu * (2/r1 - 1/a))

# Delta-v required
delta_v = v_transfer - v1

print("Delta-V required (km/s):", round(delta_v, 3))

# Plot orbits
theta = np.linspace(0, 2*np.pi, 500)

# Earth orbit
x1 = r1 * np.cos(theta)
y1 = r1 * np.sin(theta)

# Moon orbit
x2 = r2 * np.cos(theta)
y2 = r2 * np.sin(theta)

# Transfer orbit (ellipse)
theta_t = np.linspace(0, np.pi, 500)
x_t = a * np.cos(theta_t)
y_t = np.sqrt(r1*r2) * np.sin(theta_t)

plt.figure(figsize=(8,8))
plt.plot(x1, y1, label="Earth Orbit")
plt.plot(x2, y2, label="Moon Orbit")
plt.plot(x_t, y_t, label="Transfer Orbit")

plt.scatter(0, 0, label="Earth")

plt.axis("equal")
plt.legend()
plt.title("Earth to Moon Transfer Simulation")
plt.xlabel("km")
plt.ylabel("km")

plt.savefig("moon_transfer.png")

plt.show()

