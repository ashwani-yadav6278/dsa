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