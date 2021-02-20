n = int(input())

for i in range(1, n+1):
    while(True):
        if i % 3 == 0:
            print(f' {i}', end = '')
            break
        else:
            x = i
            while(x):
                if x % 10 == 3:
                    print(f' {i}', end = '')
                    break
                x = int(x/10)
            break
print()