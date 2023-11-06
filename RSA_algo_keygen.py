from primelibpy import Prime
import sympy
import math
import random
from sympy import mod_inverse


def closest_prime(num):
    distance = 0
    while True:
        if sympy.isprime(num + distance):
            return num + distance
        if sympy.isprime(num - distance):
            return num - distance
        distance += 1

def is_coprime(a, b):
    return math.gcd(a, b) == 1

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

randomNum1 = random.randint(1000000, 100000000)
randomNum2 = random.randint(1000000, 100000000)

while (randomNum1 == randomNum2):
    randomNum1 = random.randint(10000, 1000000)
    randomNum2 = random.randint(10000, 1000000)

p = closest_prime(randomNum1)
q = closest_prime(randomNum2)

n = p * q
z = (p-1) * (q-1)

# Use a fixed small value for e that's coprime to z
e = 65537
while not is_coprime(e, z):
    e += 2

d = mod_inverse(e, z)

PR = [n, d]
PU = [n, e]

M = input("Enter message to encrypt:")
print("Message = ", M)
C = encrypt_chunked(M, PU)
print("Cypher = ", C)
D = decrypt_chunked(C, PR)
print("Decrypted Message = ", D)
print(p, q, n, z, e, d)

# Citations:
# https://www.geeksforgeeks.org/check-two-numbers-co-prime-not/