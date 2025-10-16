
def missingNum(arr):
    xor = 0
    n = len(arr)
    for i in range(n):
        xor ^= arr[i]
        xor ^= (i+1)
    xor ^= (n+1)  # include the last number in range
    return xor

arr=[1,2,3,5,6,8,10]
target=14
missing=missingNum(arr); 
print("missing number is: ",missing);