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