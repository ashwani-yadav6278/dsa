target=14
arr=[2,3,5,7,8,9,10]
def twosum(target,arr):
    left=0
    right=len(arr)-1
    while(left<right):
        if((arr[left]+arr[right])>target):
            right-=1
        elif((arr[left]+arr[right])<target):
            left+=1   
        else:
            return [left,right]    
    return 0        

print(twosum(target,arr))
