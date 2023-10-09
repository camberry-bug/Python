import math

stopband_linear = 10**(-74/20)
passband_linear = 10**(-0.5/20)

def Mlp(f, fc, n):
    mag = 1 / math.sqrt(1 + (abs(f/fc)**(2*n)))
    return mag

def find_filter_order():
    n = 1  
    B = 1  
    while True:
        fc = B / ((1/(passband_linear**2)) - 1)**(1/(2*n))
        if Mlp(1.2*B, fc, n) <= stopband_linear:
            return n, fc
        n += 1

n, fc = find_filter_order()
print(f"Minimum required filter order, n: {n}")
print(f"fc as a function of B: {fc} * B")

