# Multi Dimensional Array
# [1 2 3 4 5 6] 1D
'''
1 2 3 4
5 6 7 8
9 1 2 3
4 5 6 7
''' 
# 2D array
# 3D array
# Nested Loops

oneD = [
    1 ,
    2 ,
    3
]
twoDArr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
threeDArr = [
    [[1,2,3],[1,2,3],[1,2,3]],
    [[1,2,3],[1,2,3],[1,2,3]],
    [[1,2,3],[1,2,3],[1,2,3]]
]
oneDStr = ""
for i in oneD:
    oneDStr += str(i);

twoDStr = ""
for i in twoDArr:
    for j in i:
        twoDStr += str(j)

threeDStr = ""
for i in threeDArr:
    for j in i:
        for k in j:
            threeDStr += str(k);
print(threeDStr)
