import numpy as np; import matplotlib.pyplot as plt

poles = [-1000+0j, -2000+0j, -500+60j, -500-60j]
zeros = [0-0j]

def magnitude(omega, poles, zeros):
    product_poles = 1
    product_zeros = 1
    
    for pole in poles:
        distance = abs(omega - pole)
        product_poles *= distance
        
    for zero in zeros:
        distance = abs(omega - zero)
        product_zeros *= distance
        
    return 20 * np.log10(product_zeros / product_poles)

omegas = np.logspace(1, 4, 500)  # 10^1 < Frequencies < 10^4
magnitudes = [magnitude(1j*omega, poles, zeros) for omega in omegas]

plt.figure(figsize=(10, 6))
plt.semilogx(omegas, magnitudes, label="Magnitude (dB)")
plt.title("Bode Plot")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
