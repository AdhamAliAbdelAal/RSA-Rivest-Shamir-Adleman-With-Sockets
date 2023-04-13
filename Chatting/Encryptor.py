from utils import *
from sympy import randprime
import time
class Encryptor:

    # Constructor
    def __init__(self,bits_s=170,bits_e=180,selfy=False):
        # Generate the public and private keys
        self.p=randprime(1<<bits_s,1<<bits_e)
        self.q=randprime(1<<bits_s,1<<bits_e)
        # Make sure that p and q are different
        while(self.p==self.q):
            self.q=randprime(1<<bits_s,1<<(bits_e))
        self.n=self.p*self.q
        self.fai = (self.p-1)*(self.q-1)
        # Choose e such that it is coprime with fai and less than fai gcd(x,x-1) is always 1
        self.e=self.fai-1
        # Calculate the private key
        self.d = modinv(self.e,self.fai)
        if(selfy):
            self.set_other_party_public_key(self.n,self.e)

    # Set the public key of the other party
    def set_other_party_public_key(self,n,e):
        self.other_party_n=n
        self.other_party_e=e

    # Get the public key
    def get_public_key(self):
        return (self.n,self.e)
    
    # Get the private key
    def get_private_key(self):
        return self.d
    
    # Encode a message
    def encode(self,message):
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
    
    # Encrypt a message
    def encrypt(self,message):
        cipher_text=power_mod(message,self.other_party_e,self.other_party_n)
        return cipher_text
    
    # Encrypt and encode a message
    def encrypt_and_encode(self,message):
        self.time=time.time()
        # Append spaces to the message to make it a multiple of 5
        message_len=len(message)
        if(message_len%5!=0):
            message+=' '*(5-message_len%5)
            message_len+=(5-message_len%5)
        message_encrypted=[]
        for i in range(0,message_len,5):
            message_encoded=self.encode(message[i:i+5])
            message_encrypted.append(str(self.encrypt(message_encoded)))
        message_encrypted=' '.join(message_encrypted)
        self.time=time.time()-self.time
        return message_encrypted
    
    #  Calculate the time taken to encrypt and encode a message
    def get_time(self):
        return self.time

