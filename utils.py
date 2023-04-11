def power_mod(a,b,n):
    x = 1 
    power = a%n
    for i in range(0,4300):
        bit=1<<i
        if(bit>b):
            return x
        if(bit&b):
            x*=power
            x%=n
        power*=power
        power%=n
    return x

def gcd(a,b,x,y):
    if(a==0):
        return (0,1,b)
    else:
        x_prev,y_prev,gcd_val=gcd(b%a,a,x,y)
        x=y_prev-(b//a)*x_prev
        y=x_prev
        return (x,y,gcd_val)


def modinv(a,m):
    x,y,gcd_val=gcd(a,m,0,0)
    if(gcd_val!=1):
        return -1
    else:
        return (x%m+m)%m