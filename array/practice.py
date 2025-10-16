
def intersection(arr1,arr2):
    i,j=0,0
    
    while i<len(arr1) and j<len(arr2):
        if(arr1[i]==arr2[j]):
            print(arr1[i],end=" ")
            i+=1
            j+=1
        elif(arr1[i]<arr2[j]):
            i+=1    
        else:
            j+=1
    
arr1=[1,2,3,3,4,5,6]
arr2=[2,3,3,4,5,6,7]
print("intersection: ",end=" ")
intersection(arr1,arr2)

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

def longestSum(arr1):
    for i in range(len(arr1)):
        sum=0
        for j in range(i,len(arr1)):
            sum+=arr1[j]
            

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

arr=[10,5,2,7,1,9]
k=15

def longestsubSum(arr,k):
    maxlen=0
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum+=arr[j]
            if(sum==k):
                maxlen=max(maxlen,j-i+1)
    return maxlen    

def longestsubSum(arr,k):
    hashMap={};
    sum=0
    maxlen=0
    for i, num in enumerate(arr):
        sum+=num
        if(sum==k):
            maxlen=max(maxlen,i+1)

        if (sum-k) in hashMap:
            maxlen=max(maxlen,i-hashMap[sum-k]) 

        if sum not in hashMap:
            hashMap[sum]=i 
    return maxlen      

    
print(longestsubSum(arr,k))

num =[3,3,0,99,-40]
def largest(list):
    lg_num=list[0]
    for i in range(1,len(list)):
        if(lg_num<list[i]):
            lg_num=list[i]
    return lg_num        

print(largest(list))

num=[1,4,5,3,6,7]
def sec_largest(num):
    if len(num)<2:
         return None
    lg_num=num[0]
    sec_lrg=float("-inf")
    for i in range(1,len(num)):
        if(num[i]>lg_num):
            sec_lrg=lg_num
            lg_num=num[i]
        elif(num[i]>sec_lrg and num[i]<lg_num):
            sec_lrg=num[i]
    if(sec_lrg==float("-inf")):
        return ("All values are equal")        
    return sec_lrg
print(sec_largest(num))

def sorted_arr(num):
    for i in range(1,len(num)):
        if(num[i]<num[i-1]):
            
            return False
    return True   

print(sorted_arr(num))

nums=[1,2,3,4,5,6,7]     

def duplicates(nums):
    new_ls=set()
    for i in range(len(nums)):
        new_ls.add(nums[i])

    return new_ls


def duplicates(nums):
    j=0
    for i in range(1,len(nums)):
        if(nums[i]!=nums[j]):
            nums[j+1]=nums[i]
            j+=1
    return nums[:j+1]        
 
print(duplicates(nums))

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

arr1=[1,2,3,5,6,7]
arr2=[1,2,4,5,7]

def union(arr1,arr2):
    # union_list=set(arr1).union(set(arr2))
    # return sorted(union)

    # alternative
    union_list=[]
    for num in arr1:
        union_list.append(num)

    for num in arr2:
        if num not in union_list:
            union_list.append(num)  

    return sorted(union_list)

print(union(arr1,arr2))



def intersection(arr1,arr2):
    result=[]
    visit=[0]* len(arr2)
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j] and visit[j]==0:
                result.append(arr1[i])
                visit[j]=1
                break
    return result
    # intList=[]
    # i=0 
    # j=0
    # n=len(arr1)
    # m=len(arr2)

    # while(i<n and j<m):
    #     if(arr1[i]>arr2[j]):
    #         j+=1
    #     elif(arr1[i]<arr2[j]):
    #         i+=1
    #     else:
    #         intList.append(arr1[i])
    #         i+=1
    #         j+=1

print(intersection(arr1,arr2))
# ls=[2,4,6,8,10,12,14,16]
ls=[1,-2,3,5,-3,8,-1,7,-2]
key=12
def binarySerh(ls,key):
    
    start=0
    end=len(ls)-1
    while start<end:
        mid=(start+end)//2
        if(key==ls[mid]):
            return mid
        elif(key>ls[mid]):
            start=mid+1
        else:
            end=mid-1
    return -1

print(binarySerh(ls,key)) 

def pair(arr):
    maxsum=float('-inf')
    currSum=0
    for i in range(len(arr)):
        currSum+=arr[i]
        maxsum=max(maxsum,currSum)
        if currSum<0:
            currSum=0
    return maxsum        
    
   
        


print(pair(ls))