import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
uranus_moons = pd.read_csv("uranus_moons.csv")
#input is Semi-major axis and output should be the orbital period
semi_major_axis,orbital_period = np.abs(np.asarray(uranus_moons["Semi-major axis"],dtype=np.float64)),np.abs(np.asarray(uranus_moons["Orbital period"],dtype=np.float64))
semi_major_axis = semi_major_axis * 1000
orbital_period = orbital_period * 24 * 60 * 60
uranus_moons["Semi major axis in meters"] = semi_major_axis
uranus_moons["Orbital period in seconds"] = orbital_period
semi_major_axis = semi_major_axis**3
orbital_period = np.power(orbital_period,2)
uranus_moons["Semi major axis in meters squared"] = semi_major_axis
uranus_moons["Orbital period in seconds cubed"] = orbital_period
print(semi_major_axis)
print(orbital_period)
X = np.hstack((np.ones((semi_major_axis.shape[0],1)),semi_major_axis[np.newaxis].T))
print(semi_major_axis.dot(orbital_period)-(semi_major_axis.shape[0]*(semi_major_axis.dot(orbital_period))))
print(sum(np.power(semi_major_axis,2)))
theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(orbital_period)
print(theta)
print(uranus_moons)
plt.scatter(semi_major_axis,orbital_period)
plt.plot(semi_major_axis,X.dot(theta))
plt.ylabel("Period Cubed")
plt.xlabel("Semi Major Axis Square")
plt.show()
