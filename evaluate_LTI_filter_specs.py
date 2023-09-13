import math

def find_filter_order(B):
    MLP_B = 10**(-0.5/20)  
    MLP_1_2B = 10**(-74/20)  
    
    n = 1
    while True:
        fc_B = B / ((1/MLP_B**2 - 1)**(1/(2*n)))
        MLP_calculated = 1 / math.sqrt(1 + (1.2 * B / fc_B)**(2*n))
        if MLP_calculated <= MLP_1_2B:
            return n, fc_B
        n += 1

B = float(input("Enter the passband frequency B (in Hz): "))
n, fc = find_filter_order(B)

print(f"Minimum required filter order, n: {n}")
print(f"Cutoff frequency, fc (as a function of B): {fc} Hz")
