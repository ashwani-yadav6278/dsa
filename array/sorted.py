def sorted_arr(num):
    for i in range(1,len(num)):
        if(num[i]<num[i-1]):
            
            return False
    return True   

num=[1,2,3,4,5,6,7]    
print(sorted_arr(num))

 