import numpy as np; import matplotlib.pyplot as plt

poles = [-10+0j, -1000+0j]
zeros = [0 - 0j]

def geom_magnitude_func(omega, poles, zeros):
    product_poles = 1
    product_zeros = 1
    
    for pole in poles:
        pole_dist = abs(omega - pole)
        product_poles *= pole_dist
        
    for zero in zeros:
        zero_dist = abs(omega - zero)
        product_zeros *= zero_dist

    linear_magnitude = (product_zeros / product_poles)
    dB_magnitude = 20 * np.log10(linear_magnitude)
    return dB_magnitude

omegas = np.logspace(0, 5, 500) 
dB_magnitude_array = [geom_magnitude_func(1j*omega, poles, zeros) for omega in omegas]

plt.figure(figsize=(10, 6))
plt.semilogx(omegas, dB_magnitude_array)
plt.title("Magnitude Bode Plot")
plt.xlabel("Frequency (w)")
plt.ylabel("Magnitude (dB)")
plt.grid(which="both", linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()
