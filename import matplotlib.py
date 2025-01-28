import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

daysOfExercise = np.array([7, 14, 22, 30, 40, 55])
weight = np.array([60, 59, 56, 52, 48, 45])

slope, intercept, r_value, p_value, std_err = linregress(daysOfExercise, weight)

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R_squared: {r_value**2}")

reg_line = slope * daysOfExercise + intercept

plt.scatter(daysOfExercise, weight, color = 'green', label = 'Data')
plt.plot(daysOfExercise, reg_line, color = 'red', label = 'Regression Line')

plt.xlabel('Days of Exercise')
plt.ylabel('Weight Loss')
plt.title('Weight Progress')
plt.legend()

plt.show()