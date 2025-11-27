
fruits=["mango","orange","banana","apple"]

def largest(fruits):
    largestStr=fruits[0]
    for i in range(0,len(fruits)):
        if(largestStr<fruits[i]):
            largestStr=fruits[i]
    return largestStr 
    
a=largest(fruits)
print(a)    