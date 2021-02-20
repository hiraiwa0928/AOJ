while(True):
    h, w = map(int, input().split())
    
    if h == 0 and w == 0:
        exit()
    
    for i in range(h):
        flag = 1 if i%2 == 0 else 0
        for j in range(w):

            if flag == 1:
                print('#', end = '')
            else:
                print('.', end = '')
            
            flag = 0 if flag else 1
        print('')
    print('')
