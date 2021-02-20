s = list(str(input()))

for num, ele in enumerate(s):
    ele = str(ele)
    if(ele.islower()):
        s[num] = ele.upper()
    else:
        s[num] = ele.lower()
    
    print(f'{s[num]}', end = '')
    
print()
