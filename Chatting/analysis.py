from Encryptor import Encryptor
from Decryptor import Decryptor
import numpy as np
import matplotlib.pyplot as plt

n_bits = range(160,1200,20)
# print(n_bits)
encryption_time=np.zeros(len(n_bits))
decryption_time=np.zeros(len(n_bits))

plain_text = "hello"

for i in range(len(n_bits)):
    print(n_bits[i])
    encryptor = Encryptor(n_bits[i],n_bits[i]+1,True)
    cipher_txt=encryptor.encrypt_and_encode(plain_text)
    encryption_time[i]=encryptor.get_time()
    # Get the public key
    n,_=encryptor.get_public_key()

    # Get the private key
    d=encryptor.get_private_key()

    decryptor = Decryptor(n,d)
    decryptor.decrypt_and_decode(cipher_txt)
    decryption_time[i]=decryptor.get_time()

plt.scatter(n_bits,encryption_time,c="r",label="Encryption time",marker='x',s=15)
plt.scatter(n_bits,decryption_time,c="b",label="Decryption time",marker='o',s=15)
plt.xlabel("number of bits of n")
plt.ylabel("Time(seconds)")
plt.title("Encryption and decryption time")
plt.legend()
plt.tight_layout()
plt.show()