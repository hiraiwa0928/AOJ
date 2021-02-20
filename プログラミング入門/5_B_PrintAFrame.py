while(True):
    h, w = map(int, input().split())
    
    if h == 0 and w == 0:
        exit()
    
    for i in range(h):
        for j in range(w):
            if i == 0 or j == 0 or i == h-1 or j == w-1:
                print('#', end = '')
            else:
                print('.', end = '')
        print('')
    print('')
