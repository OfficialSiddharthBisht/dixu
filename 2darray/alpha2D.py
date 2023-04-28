twoDArr=[
    ["a","b","c"],
    ["d","e","f"],
    ["g","h","i"]
]
twoDStr = ""
for i in twoDArr:
    for j in i:
        twoDStr += str(j)
print(twoDStr)