import  numpy as np
n= int(input())
while(n!=0):
    s = 0
    x = int(input())
    array = [[0 for i in range(x)]for p in range(x)]
    for i in range(0,2*x-2):
        for j in range(0,x):
            for k in range(0,x):
                if((j+k)==i):
                    s = s+1
                    array[j][k] = s
    for i in range(0,x):
        for j in range(0,x):
            print(array[i][j],end=" ")
        print("\n")
    n=n-1 