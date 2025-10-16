num =[3,3,0,99,-40]
def largest(list):
    lg_num=list[0]
    for i in range(1,len(list)):
        if(lg_num<list[i]):
            lg_num=list[i]
    return lg_num        

print(largest(num))
