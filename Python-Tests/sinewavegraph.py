#Generated by ChatGPT

import numpy as np
import matplotlib.pyplot as plt

# Get user input for sine parameters
amplitude = float(input("Enter the amplitude of the sine wave: "))
frequency = float(input("Enter the frequency of the sine wave (in Hz): "))
phase = float(input("Enter the phase shift of the sine wave (in radians): "))
vertical_shift = float(input("Enter the vertical shift of the sine wave: "))

# Generate x-values for the sine wave
x = np.linspace(0, 2*np.pi, 1000)

# Calculate y-values for the sine wave based on user input
y = amplitude * np.sin(2*np.pi*frequency*x + phase) + vertical_shift

# Plot the sine wave
plt.plot(x, y)

# Add labels and a title to the graph
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine Wave')

# Display the graph
plt.show()
