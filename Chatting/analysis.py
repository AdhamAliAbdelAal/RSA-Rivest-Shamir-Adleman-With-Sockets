from Encryptor import Encryptor
from Decryptor import Decryptor
import numpy as np

n_bits = np.arange(150,1000)
encryption_time=np.zeros(len(n_bits))
decryption_time=np.zeros(len(n_bits))

plain_text = "hello"

for i in range(len(n_bits)):
    encryptor = Encryptor(n_bits[i])
    encryptor.encrypt(plain_text)
    encryption_time[i]=encryptor.time
    decryptor = Decryptor(encryptor.e,encryptor.n,encryptor.cipher_text)
    decryptor.decrypt()
    decryption_time[i]=decryptor.time