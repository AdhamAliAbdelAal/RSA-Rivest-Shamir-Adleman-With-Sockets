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
        return (0,1,a)
    else:
        x_prev,y_prev,gcd_val=gcd(b%a,a,x,y)
        x=y_prev-(b//a)*x_prev
        y=x_prev
        return (x,y,gcd_val)
print(gcd(2,5,1,1))


