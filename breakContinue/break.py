# break -> to get out of a loop -> condition
arr = [1,3,3,7,5,6,7,8,9]
N = len(arr)
upperLimit = 99999;
for i in range(0, N):
    if(i > upperLimit):
        break;
    print(i,arr[i])
# infinite loop