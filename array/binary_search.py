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
ls=[1,3,5,6,8,12,14,15,18]