x=4
arr=[[0 for i in range(2*x-1)] for y in range(x)]
arr[0][(2*x-1)//2]=1
for i in range(1,x):
    for j in range(2*x-1):
        if(j==2*x-2):
            arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
        else:
            arr[i][j]=arr[i-1][j-1]+arr[i-1][j+1]

for i in range(x):
    for j in range(2*x-1):
        if(arr[i][j]==0):
            print(' ',end="")
        else:
            print(arr[i][j],end="")
    print()
        