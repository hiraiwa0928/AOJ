x, y = map(int, input().split())

# xのほうが値が大きくなるようにする
if x < y:
    x, y = y, x

while (True): 
    if x % y == 0:
        break
    num = int(x/y)
    tmp = y
    y = x % (y*num)
    x = tmp

print(y)