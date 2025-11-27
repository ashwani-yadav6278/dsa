s="ashwani"

def substr(s,start,end):
    substring=""
    for i in range(start,end):
        substring+=s[i]
    return substring
    

a=substr(s,1,5)        
print(a)