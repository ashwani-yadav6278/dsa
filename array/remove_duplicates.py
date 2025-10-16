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

nums=[1,2,3,2,4,5,6]