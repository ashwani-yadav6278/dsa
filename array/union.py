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

