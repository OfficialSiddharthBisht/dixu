def functionName(arr):
    sum = 0
    # only print the sum of even numbers
    for i in arr:
        for j in i:
            if j%2==0:
                sum=sum+j
    return sum


arr1 = [
    [1,6,54],
    [22,29,5],
    [87,52,65]
]
arr2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(functionName(arr1))
print(functionName(arr2))