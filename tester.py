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
def H(f):
    return 0.155 * (1 / (1/0.0003 - 1j*2*np.pi*(5000-f)) - 1 / (1/0.0003 + 1j*2*np.pi*(5000+f)))

# Generate frequency values from 0 to 500KHz
frequencies = np.logspace(0, np.log10(500e3), 1000)

# Evaluate the frequency response
response = H(frequencies)

# Convert to amplitude in decibels
amplitude_dB = 20 * np.log10(np.abs(response))

# Plot
plt.semilogx(frequencies, amplitude_dB)
plt.title('Amplitude of Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.grid(True, which="both", ls="--")
plt.xlim([frequencies[0], frequencies[-1]])
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Define the frequency response function
def H(w):
    return 10000 / (10000 + 1j*w)

# Generate frequency values from 0 to 500KHz
frequencies = np.linspace(0, 500e3, 1000)

# Evaluate the frequency response
response = H(2 * np.pi * frequencies)  # 2*pi*f is the angular frequency

# Convert to amplitude in decibels
amplitude_dB = 20 * np.log10(np.abs(response))

# Plot
plt.semilogx(frequencies, amplitude_dB)
plt.title('Amplitude of Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.grid(True, which="both", ls="--")
plt.xlim([frequencies[1], frequencies[-1]])  # Start from the second frequency to avoid log(0)
plt.show()
