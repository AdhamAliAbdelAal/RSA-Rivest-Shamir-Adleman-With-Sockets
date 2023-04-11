from encryption_model import *
import time
import matplotlib.pyplot as plt
import numpy as np
plain_text = "hello"
def factorize(n):
    i=2
    while(i*i<=n):
        if(n%i==0):
            return i,n//i
        i+=1
def attack(e,n,cipher_text):
    # Get the factors of n
    p,q=factorize(n)
    # Calculate fai
    fai = (p-1)*(q-1)
    # Calculate the private key
    d=modinv(e,fai)
    # Decrypt the message
    return decrypt(int(cipher_text),d,n)
n_bits = range(15,27)
breaking_cipher_time = []
for i in n_bits:
    e,n,cipher_text = encrypt_black_box(plain_text,i)
    print(e,n,cipher_text)
    start_time = time.time()
    decrypted_message = attack(e,n,cipher_text)
    breaking_cipher_time.append(time.time()-start_time)
    print(decoder(decrypted_message))

plt.plot(np.array(n_bits[:len(breaking_cipher_time)])*2,breaking_cipher_time,marker="x",c="r")
plt.xlabel("number of bits of n")
plt.ylabel("Time(seconds)")
plt.title("Breaking cipher time")
plt.tight_layout()
plt.show()