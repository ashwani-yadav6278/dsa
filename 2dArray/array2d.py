
# rows=int(input("enter rows number: "))
# cols=int(input("enter cols number: "))
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# when we take input from user

# for i in range(rows):
#     print(f"enter {cols} numbers for row{i+1} (sapce separated): ")
#     row=list(map(int, input().split()))

#     if len(row) !=cols:
#         print("Invalid input! please enter exacctly",cols, "values")
#         exit()
#     matrix.append(row)

# n=len(matrix)
# for i in range(n):
#     for j in range(len(matrix[0])):
#         print(f'({i},{j})',end=" ")
#     print()


#  print spiral of matrix

ls=[[1,2,3,4],
    [5,6,7,8,],
    [9,10,11,12],
    [13,14,15,16]]

def spiral(ls):
    sRow=0
    eRow=len(ls)-1
    sCol=0
    eCol=len(ls[0])-1

    while (sRow<= eRow and sCol<=eCol):
        #  top boundary
        for i in range(sCol,eCol+1):
            print(ls[sRow][i],end=",")
        #   right
        for i in range(sRow+1,eRow+1):
            print(ls[i][eCol],end=",")
        #   Bottom
         
        for i in range(eCol-1,sCol-1,-1):
            if(sRow==eRow):
                break;
            print(ls[eRow][i],end=",")
        # left    
        for i in range(eRow-1,sRow,-1):
            if(sCol==eCol):
                break;
            print(ls[i][sCol],end=",")    
        sRow+=1
        eRow-=1
        sCol+=1
        eCol-=1

spiral(ls)



