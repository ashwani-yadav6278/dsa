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

def longestSum(arr1):
    max_sum = arr1[0]
    current_sum = 0
    
    for num in arr1:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:   # Reset if negative
            current_sum = 0

    return max_sum

arr1 = [1, 5, 8, 9, 12, 13, 15]
print(longestSum(arr1))
