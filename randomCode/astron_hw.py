import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import six
from fpdf import FPDF
uranus_moons = pd.read_csv("uranus_moons.csv")
#input is Semi-major axis and output should be the orbital period
semi_major_axis,orbital_period = np.abs(np.asarray(uranus_moons["Semi-major axis"],dtype=np.float64)),np.abs(np.asarray(uranus_moons["Orbital period"],dtype=np.float64))
semi_major_axis = semi_major_axis * 1000
orbital_period = orbital_period * 24 * 60 * 60
uranus_moons["Semi-major axis in meters"] = semi_major_axis
uranus_moons["Orbital period in seconds"] = orbital_period
semi_major_axis = semi_major_axis**3
orbital_period = np.power(orbital_period,2)
uranus_moons["Semi-major axis in meters squared"] = semi_major_axis
uranus_moons["Orbital period in seconds cubed"] = orbital_period
print(semi_major_axis)
print(orbital_period)
X = np.hstack((np.ones((semi_major_axis.shape[0],1)),semi_major_axis[np.newaxis].T))
print(semi_major_axis.dot(orbital_period)-(semi_major_axis.shape[0]*(semi_major_axis.dot(orbital_period))))
print(sum(np.power(semi_major_axis,2)))
theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(orbital_period)
print(theta)
print(uranus_moons)
mass_of_uranus = (4*(3.14**2))/((6.674*(10**-11))*theta[1])
print(mass_of_uranus)
fig,ax = plt.subplots()
plt.scatter(semi_major_axis,orbital_period)
plt.plot(semi_major_axis,X.dot(theta))
plt.ylabel("Period Cubed")
plt.xlabel("Semi Major Axis Square")
plt.savefig("linechart.png")
uranus_moons.to_csv("output.csv")
pdf = FPDF()
pdf.add_page()
pdf.set_xy(10,10)
pdf.set_font('arial','B',11)
pdf.cell(0,0,"Using Least Squares Linear regression and Kepler's third law to find the mass of Uranus")
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(-20)
pdf.cell(0,0,"Ian Gomez")
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(-160)
pdf.cell(0,0,"I pledge my honor that I have abided by the Stevens honor System - igomez1 10428821")
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(-17)
pdf.cell(0,0,"Section B")
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(-13)
pdf.cell(0,0,"10/9/19")
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(-190)
pdf.cell(0,0,"T^2 = " + str(theta[1])[:6] + str(theta[1])[-4:]+ " * R^3 + 8.907e+7")
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(-190)
pdf.cell(0,0,"The mass of uranus is "+str(mass_of_uranus)[:5]+str(mass_of_uranus)[-4:])
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(-200)
pdf.image("linechart.png",x=None,y=None,w=0,h=0,type='',link='')
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(-190)
pdf.output("Lab_Uranus.pdf","F")
