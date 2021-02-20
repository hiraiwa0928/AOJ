import math
n = int(input())

cnt = 0

for i in range(n):
    num = int(input())
    flag = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            flag = 0
            break
    if flag == 1:
        cnt += 1
    
print(cnt)