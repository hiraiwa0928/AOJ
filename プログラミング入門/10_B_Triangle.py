import math
a, b, c = map(float, input().split())

s = a*b*math.sin(c/180*math.pi)/2
L = a + b + math.sqrt(a**2+b**2-2*a*b*math.cos(c/180*math.pi))
h = b*math.sin(c/180*math.pi)

print(f'{s:.5f}')
print(f'{L:.5f}')
print(f'{h:.5f}')