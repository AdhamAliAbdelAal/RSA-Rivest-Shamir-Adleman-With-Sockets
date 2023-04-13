from utils import *
from sympy import randprime
import time
class Encryptor:

    # Constructor
    def __init__(self,bits_s=170,bits_e=180,selfy=False):
        # Generate the public and private keys
        self.__p=randprime(1<<bits_s,1<<bits_e)
        self.__q=randprime(1<<bits_s,1<<bits_e)
        # Make sure that p and q are different
        while(self.__p==self.__q):
            self.__q=randprime(1<<bits_s,1<<(bits_e))
        self.__n=self.__p*self.__q
        self.__fai = (self.__p-1)*(self.__q-1)
        # Choose e such that it is coprime with fai and less than fai gcd(x,x-1) is always 1
        self.__e=self.__fai-1
        # Calculate the private key
        self.__d = modinv(self.__e,self.__fai)
        if(selfy):
            self.__set_other_party_public_key(self.__n,self.__e)

    # Set the public key of the other party
    def set_other_party_public_key(self,n,e):
        self.__other_party_n=n
        self.__other_party_e=e

    # Get the public key
    def get_public_key(self):
        return (self.__n,self.__e)
    
    # Get the private key
    def get_private_key(self):
        return self.__d
    
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
        cipher_text=power_mod(message,self.__other_party_e,self.__other_party_n)
        return cipher_text
    
    # Encrypt and encode a message
    def encrypt_and_encode(self,message):
        self.__time=time.time()
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
        self.__time=time.time()-self.__time
        return message_encrypted
    
    #  Calculate the time taken to encrypt and encode a message
    def get_time(self):
        return self.__time

