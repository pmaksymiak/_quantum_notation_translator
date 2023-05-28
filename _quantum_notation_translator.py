#TRANSLATION OF BLOCH SPHERE INTO THE COMPUTATIONAL NOTATION
import numpy as np

def decode_bloch_sphere(theta, phi):
    # Calculate the amplitudes
    a = np.cos(theta / 2)
    b = np.exp(1j * phi) * np.sin(theta / 2)
    
    # Return the state in the computational basis
    return a, b

# Test the function
theta = 1.649
phi = 4.932
a, b = decode_bloch_sphere(theta, phi)

# Print the Bloch sphere coordinates and their meaning
print(f"Bloch sphere coordinates: θ={theta}, ϕ={phi}")
print("These are the polar and azimuthal angles that determine the state of the qubit on the Bloch sphere.")
print("θ (theta) is the polar angle (from the positive z-axis).")
print("ϕ (phi) is the azimuthal angle (from the positive x-axis).")

# Print the state in the computational basis and its meaning
print(f"\nState in the computational basis: |qubit⟩ = {a} |0⟩ + {b} |1⟩")
print("This is the state of the qubit in the computational basis, which is a superposition of the |0⟩ and |1⟩ states.")
print("The complex numbers give the amplitudes of the |0⟩ and |1⟩ states.")
print("The absolute square of the amplitude gives the probability of measuring the qubit in that state.")

# Calculate and print the probabilities
p0 = np.abs(a)**2
p1 = np.abs(b)**2
print(f"\nProbability of measuring |0⟩: {p0}")
print(f"Probability of measuring |1⟩: {p1}")

# Print the calculations
print("\nCalculations:")
print(f"The amplitude of the |0⟩ state is a real number: {a}.")
print(f"The amplitude of the |1⟩ state is a complex number: {b}.")
print(f"The probability of measuring the |0⟩ state is the absolute square of its amplitude: |{a}|^2 = {p0}.")
print(f"The probability of measuring the |1⟩ state is the absolute square of its amplitude: |{b}|^2 = {p1}.")
