# Input test cases
print("Enter test cases (T): ")
t = int(input())

while (t > 0):
    t -= 1

    print("Enter number of elements (N): ")
    N = int(input())

    print("Enter elements separated by spaces: ")
    arr = list(map(int, input().split()))

    # assign the values of array in different variables
    a = arr[0]
    b = arr[1]
    c = arr[2]
    d = arr[3]

    # compare the difference between the array element
    if (b - a == c - b): #find common difference
        diff = b - a
    elif(c - b == d - c):
        diff = c - b
    else :
        diff = d - a //3;

    ref = arr[0]
    
    #compare common difference with the array elements
    for i in range(1, N): 
        if (ref + diff == arr[i]):
            ref = ref + diff
        #print the wrong element in array
        else :
            print("Wrong term/number: ")
            print(arr[i])
            break
