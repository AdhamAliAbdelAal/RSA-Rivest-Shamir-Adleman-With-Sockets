from utils import *
from sympy import randprime
import random
def encrypt(plain_text,e,n):
    cipher_text=power_mod(plain_text,e,n)
    return cipher_text

def decrypt(cipher_text,d,n):
    plain_text=power_mod(cipher_text,d,n)
    return plain_text


def encoder(message):
    result= 0
    for (i,c) in enumerate(message):
        if(c>='0' and c<='9'):
            val=ord(c)-ord('0')
        elif(c>='a' and c<='z'):
            val=ord(c)-ord('a')+10
        else:
            val=36
        result+=val*(37**i)
    return result

def decoder(message):
    result=""
    while(message>0):
        val=message%37
        if(val>=0 and val<=9):
            result+=chr(val+ord('0'))
        elif(val>=10 and val<=35):
            result+=chr(val+ord('a')-10)
        else:
            result+=' '
        message=message//37
    return result

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






