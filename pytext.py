import math
def main():
    q=eval(input('输入q的值：'))
    s=0
    n=1
    a=1
    while abs(a)<10^(-6):
        s=s+a
        a=a*q^(1-n)
        n=n+1        
    print("s={},n={}".format(s,n))

    
main()
