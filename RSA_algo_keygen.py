from primelibpy import Prime
import random

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def closest_prime(n):
    """Find the closest prime to a number."""
    distance = 0
    while True:
        if is_prime(n + distance):
            return n + distance
        if is_prime(n - distance):
            return n - distance
        distance += 1


# Get larger primes for security
randomNum1 = random.randint(1000000, 100000000)
randomNum2 = random.randint(1000000, 100000000)

while (randomNum1 == randomNum2):
    randomNum1 = random.randint(10000, 1000000)
    randomNum2 = random.randint(10000, 1000000)

p = closest_prime(randomNum1)
q = closest_prime(randomNum2)

n = p * q
z = (p-1) * (q-1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_coprime(a, b):
    return gcd(a, b) == 1
# Use a fixed small value for e that's coprime to z
e = 65537
while not is_coprime(e, z):
    e += 2

# Extended Euclidean Algorithm to find d
m0, x0, x1 = z, 0, 1
a, m = e, z
while a > 0 and m > 0:
    q = a // m
    a, m = m, a % m
    x0, x1 = x1 - q * x0, x0
d = x1 % m0

PR = [n, d]
PU = [n, e]

def encrypt(Message, PU):
    M = int.from_bytes(Message.encode(), 'big')  # Convert string to integer
    Cyphertext = pow(M, PU[1], PU[0])
    return Cyphertext

def decrypt(Cyphertext, PR):
    Message = pow(Cyphertext, PR[1], PR[0])
    return Message.to_bytes((Message.bit_length() + 7) // 8, 'big').decode()

def encrypt_chunked(Message, PU):
    chunks = Message.split(' ')  # Split message into chunks based on spaces
    encrypted_chunks = [encrypt(chunk, PU) for chunk in chunks]
    return encrypted_chunks

def decrypt_chunked(encrypted_chunks, PR):
    decrypted_chunks = [decrypt(chunk, PR) for chunk in encrypted_chunks]
    return ' '.join(decrypted_chunks)

# Test
M = input("Enter message to encrypt:")
print("Message = ", M)
C = encrypt_chunked(M, PU)
print("Cypher = ", C)
D = decrypt_chunked(C, PR)
print("Decrypted Message = ", D)
print(p, q, n, z, e, d)
