arr = [1,2,3]

for i in range(0,len(arr)):
    print("for",arr[i])

N = len(arr)
i = 0
while (i > N):
    print("while",arr[i])

while True:
    if(i < N):
        break
    print("infinite while",arr[i])