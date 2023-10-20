import numpy as np
import matplotlib.pyplot as plt

# Define the impulse response function
def h(t):
    return 0.31 * np.exp(-t/0.0003) * np.sin(2*np.pi*5000*t)

# Generate time values
t = np.linspace(0, 0.002, 1000)

# Evaluate the impulse response
response = h(t)

# Plot
plt.plot(t, response)
plt.title('Impulse Response')
plt.xlabel('Time (s)')
plt.ylabel('h(t)')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Define the Fourier transform function
j=1j
def H1(f): 
    return (10**5)*0.31* ((((2*np.pi*5000)))/(((1/0.0003)+(j*2*np.pi*f))**2+(2*np.pi*5000)**2))
 
# Frequency range
frequencies1 = np.logspace(0, np.log10(500e3), 1000)  # From 1Hz to 500KHz
# Calculate the amplitude response
amplitude_response1 = np.abs(H1(frequencies1))
# Convert amplitude to decibels
amplitude_db1 = 20 * np.log10(amplitude_response1)

# Plot
plt.figure(figsize=(10, 6))
plt.semilogx(frequencies1, amplitude_db1)
plt.title("Amplitude Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (dB)")
plt.grid(True, which="both", ls="--")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Define the frequency response function
def H2(f):
    return 10000 / (10000 + 1j*2*np.pi*f)

# Generate frequency values from 0 to 500KHz
frequencies2 = np.logspace(0, np.log10(500e3), 1000)

# Evaluate the frequency response
response2 = H2( frequencies2)  # 2*pi*f is the angular frequency

# Convert to amplitude in decibels
amplitude_dB2 = 20 * np.log10(np.abs(response2))

# Plot
plt.semilogx(frequencies2, amplitude_dB2)
plt.title('Amplitude of Frequency Response: 10000 / (10000 + 1j*w)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.grid(True, which="both", ls="--")
plt.xlim([frequencies2[1], frequencies2[-1]])  # Start from the second frequency to avoid log(0)
plt.show()

# Evaluate the frequency response
Final_response = H2(frequencies2)*H1(frequencies1)  # 2*pi*f is the angular frequency

# Convert to amplitude in decibels
final_amplitude_dB = 20 * np.log10(np.abs(Final_response))

# Plot
plt.semilogx(frequencies2, final_amplitude_dB)
plt.title('Cascade Amplitude of Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.grid(True, which="both", ls="--")
plt.xlim([frequencies2[1], frequencies2[-1]])  # Start from the second frequency to avoid log(0)
plt.show()