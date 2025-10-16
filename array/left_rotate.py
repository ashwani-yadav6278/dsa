def left_by_k(nums,k):
    temp=[]
    n=len(nums)
    for i in range(k):
        temp.append(nums[i])

    for i in range(k,n):
        nums[i-k]=nums[i]    

    for i in range(n-k,n):
        nums[i]=temp[i-(n-k)]  

    return nums
print(left_by_k(nums,k=3))
def rotate( nums, k):

    n=len(nums)
    temp=[]
    for i in range(n-k):
        temp.append(nums[i])
    print(temp)    
    for i in range(n-k,n):
        nums[i-(n-k)]=nums[i]
    j=0    
    for i in range(k,n):
        nums[i]=temp[j]
        j+=1     
    return nums         

# rotate(nums,3)
print (rotate(nums,3))