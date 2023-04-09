from utils import *
from sympy import randprime
import random
def encrypt_black_box(message,n_bits):
    message=encoder(message)
    p,q=generate_two_primes(n_bits)
    n=p*q
    while(n<message):
        p,q=generate_two_primes(n_bits)
        n=p*q
    fai = (p-1)*(q-1)
    e=random.randint(1,fai)
    # Check if e is coprime with fai
    while(gcd(e,fai,0,0)[2]!=1):
        e=random.randint(1,fai)
    return e,n,str(encrypt(message,e,n))

def generate_two_primes(n_bits):
    # Generate the public and private keys
    p=randprime(1<<n_bits,1<<(n_bits+1))
    q=randprime(1<<n_bits,1<<(n_bits+1))
    # Make sure that p and q are different
    while(p==q):
        q=randprime(1<<n_bits,1<<(n_bits+1))
    return p,q






