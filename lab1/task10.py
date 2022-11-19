a = int(input())
b = int(input())
c = int(input())
d=[a, b, c]
f=[]
for i in range(0,3):
    f.append(min(d))
    d.remove(min(d))
print(f[0],f[1],f[2])
