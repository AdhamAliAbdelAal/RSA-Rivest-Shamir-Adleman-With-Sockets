from utils import *
class Decryptor:
    # Constructor
    def __init__(self,n,d):
        self.n=n
        self.d=d

    # Decode a message
    def decode(self,message):
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
    
    # Decrypt a message
    def decrypt(self,message):
        plain_text=power_mod(message,self.d,self.n)
        return plain_text
    
    # Decrypt and decode a message
    def decrypt_and_decode(self,encrypted_message):
        # Get the number of sets of 5 characters
        encrypted_message=encrypted_message.split(' ')
        message_sets_len=len(encrypted_message)
        message=''
        for i in range(message_sets_len):
            decrypted_block=decrypt(int(encrypted_message[i]),self.d,self.n)
            message+=decoder(decrypted_block)   
        return message
    