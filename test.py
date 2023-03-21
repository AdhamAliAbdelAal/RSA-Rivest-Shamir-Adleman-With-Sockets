# import signal
# import sys

# def signal_handler(sig, frame):
#     print('You pressed Ctrl+C!')
#     sys.exit(0)

# signal.signal(signal.SIGINT, signal_handler)
# print('Press Ctrl+C')

# def encoder(message):
#     result= 0
#     for (i,c) in enumerate(message):
#         if(c>='0' and c<='9'):
#             val=ord(c)-ord('0')
#         elif(c>='a' and c<='z'):
#             val=ord(c)-ord('a')+10
#         else:
#             val=36
#         result+=val*(37**i)
#     return result

# print(encoder("hello"))
def gcd(a,b,x,y):
    if(a==0):
        return (0,1,b)
    else:
        x_prev,y_prev,gcd_val=gcd(b%a,a,x,y)
        x=y_prev-(b//a)*x_prev
        y=x_prev
        return (x,y,gcd_val)
p=319993
q= 999331
n=p*q
e=n-2
fai = (p-1)*(q-1)
print(gcd( e,fai,1,1))
#print(1<<4300)

# def power_mod(a,b,n):
#     x = 1 
#     power = a%n
#     for i in range(0,4300):
#         bit=1<<i
#         if(bit>b):
#             return x
#         if(bit&b):
#             x*=power
#             x%=n
#         power*=power
#         power%=n
#     return x
# print(power_mod(55,96,1234))


