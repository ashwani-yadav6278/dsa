height=[0,1,0,2,1,0,1,3,2,1,2,1]
n=len(height)
left_max=[0] * n
right_max=[0] * n
right_max[n-1]=height[n-1]
left_max[0]=height[0]

# LeftMax array
for i in range(1,n):
    left_max[i]=max(height[i],left_max[i-1])
# RightMax array
for i in range(n-2,-1,-1):
    right_max[i]=max(height[i],right_max[i+1])

trapped_water=0
for i in range(n):
    waterlevel=min(right_max[i],left_max[i])
    trapped_water += (waterlevel) - (height[i])    

print(trapped_water)

