n=int(input("Enter a number \n"))

isPrime=True
if(n>1):
        
    for i in range(2,n):
        if(n % i==0):
            isPrime=False
            break

print(isPrime)            