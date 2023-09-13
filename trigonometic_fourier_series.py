from sympy import symbols, integrate, sin, pi, cos; from sympy import *; import numpy as np; import matplotlib.pyplot as plt

t, n, T, tau = symbols('t n T tau', real=True, positive=True)

A = 1/tau
T=1

x1 = - ((A/tau)*t) + A  # 0 <= t <= tau

f0 = 1/T
a0_1 = 1/2
an_1 = 2/T * integrate(x1 * cos(2*pi*n*f0*t), (t, 0, tau))
bn_1 = 2/T * integrate(x1 * sin(2*pi*n*f0*t), (t, 0, tau))

an_values_50=[0] *8
bn_values_50=[0] *8
an_mag_50=[0] *8
an_phase_50=[0] *8

an_values_6=[0] *8
bn_values_6=[0] *8
an_mag_6=[0] *8
an_phase_6=[0] *8

an_values_1=[0] *8
bn_values_1=[0] *8
an_mag_1=[0] *8
an_phase_1=[0] *8

for val in range(0,9):
    an_values_50[val-1] = an_1.evalf(subs={tau:1/50, n:val})
    bn_values_50[val-1] = bn_1.evalf(subs={tau:1/50, n:val})

for val in range(0,9):
    an_values_6[val-1] = an_1.evalf(subs={tau:1/6, n:val})
    bn_values_6[val-1] = bn_1.evalf(subs={tau:1/6, n:val})

for val in range(0,9):
    an_values_1[val-1] = an_1.evalf(subs={tau:1, n:val})
    bn_values_1[val-1] = bn_1.evalf(subs={tau:1, n:val})

for val in range(8):  # Since the arrays are of size 8
    an_mag_50[val] = np.sqrt(float(an_values_50[val])**2 + float(bn_values_50[val])**2)
    an_mag_6[val] = np.sqrt(float(an_values_6[val])**2 + float(bn_values_6[val])**2)
    an_mag_1[val] = np.sqrt(float(an_values_1[val])**2 + float(bn_values_1[val])**2)

for val in range(8):  # Since the arrays are of size 8
    an_phase_50[val] = -np.arctan2(float(bn_values_50[val]), float(an_values_50[val]))
    an_phase_6[val] = -np.arctan2(float(bn_values_6[val]), float(an_values_6[val]))
    an_phase_1[val] = -np.arctan2(float(bn_values_1[val]), float(an_values_1[val]))

harmonics = list(range(1, 9))

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.stem(harmonics, an_mag_50, use_line_collection=True)
plt.title('Magnitude Spectrum for tau=1/50')
plt.xlabel('Harmonic Number')
plt.ylabel('Magnitude')
plt.subplot(1, 3, 2)
plt.stem(harmonics, an_mag_6, use_line_collection=True)
plt.title('Magnitude Spectrum for tau=1/6')
plt.xlabel('Harmonic Number')
plt.ylabel('Magnitude')
plt.subplot(1, 3, 3)
plt.stem(harmonics, an_mag_1, use_line_collection=True)
plt.title('Magnitude Spectrum for tau=1')
plt.xlabel('Harmonic Number')
plt.ylabel('Magnitude')
plt.tight_layout()
plt.show()

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.stem(harmonics, an_phase_50, use_line_collection=True)
plt.title('Phase Spectrum for tau=1/50')
plt.xlabel('Harmonic Number')
plt.ylabel('Phase (radians)')
plt.subplot(1, 3, 2)
plt.stem(harmonics, an_phase_6, use_line_collection=True)
plt.title('Phase Spectrum for tau=1/6')
plt.xlabel('Harmonic Number')
plt.ylabel('Phase (radians)')
plt.subplot(1, 3, 3)
plt.stem(harmonics, an_phase_1, use_line_collection=True)
plt.title('Phase Spectrum for tau=1')
plt.xlabel('Harmonic Number')
plt.ylabel('Phase (radians)')
plt.tight_layout()
plt.show()

time_values = np.linspace(0, 3, 1000)  

def reconstruct_signal(time_values, a0, an_values, bn_values, f0):
    reconstructed_signal = np.full_like(time_values, float(a0))
    for n, (an, bn) in enumerate(zip(an_values, bn_values), start=1):
        reconstructed_signal += float(an) * np.cos(2 * np.pi * n * f0 * time_values)
        reconstructed_signal += float(bn) * np.sin(2 * np.pi * n * f0 * time_values)
    return reconstructed_signal

signal_50 = reconstruct_signal(time_values, a0_1, an_values_50, bn_values_50, f0)
signal_6 = reconstruct_signal(time_values, a0_1, an_values_6, bn_values_6, f0)
signal_1 = reconstruct_signal(time_values, a0_1, an_values_1, bn_values_1, f0)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.plot(time_values, signal_50)
plt.title('Reconstructed Signal for tau=1/50')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.subplot(1, 3, 2)
plt.plot(time_values, signal_6)
plt.title('Reconstructed Signal for tau=1/6')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.subplot(1, 3, 3)
plt.plot(time_values, signal_1)
plt.title('Reconstructed Signal for tau=1')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()