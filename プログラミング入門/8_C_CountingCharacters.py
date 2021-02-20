alp = 'abcdefghijklmnopqrstuvwxyz'
c = [0] * len(alp)

while(True):
    try:
        s = str(input()).lower() # 小文字に変換できなかったらbreak
    except:
        break
    
    for i in range(len(alp)):
        c[i] += s.count(alp[i])

for num, ele in enumerate(alp):
    print(f'{alp[num]} : {c[num]}')