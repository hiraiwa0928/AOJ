while(1):
    a, ope, b = map(str, input().split())
    a = int(a)
    b = int(b)
    
    if ope == '+':
        print(a+b)
    elif ope == '-':
        print(a-b)
    elif ope == '*':
        print(a*b)
    elif ope == '/':
        print(int(a/b))
    else:
        exit()