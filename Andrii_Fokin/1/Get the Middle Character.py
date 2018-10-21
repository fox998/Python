inStr = str(input())

size = len(inStr)
if size % 2:
    outStr = inStr[size // 2]
else:
    size //= 2
    outStr = inStr[size - 1: size + 1]
print(outStr)