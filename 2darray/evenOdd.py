num = [
    [1,6,54],
    [22,29,5],
    [87,52,65]
]
even = []
odd = []
evenStr = ""
for i in num:
    for j in i:
        if j%2==0:
            even.append(j)
        else:
            odd.append(j)
print(even,odd)