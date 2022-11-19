a=int(input())
n=0
for i in range(1,a+1):
    n=n+45
for i in range(1,a):
    if i % 2 == 0:
        n=n+15
    if i%2==1:
        n=n+5

n=n+540
m=n%60
h=int(n/60)
running=True
while running:
    if h>23:
        h=h-24
    else:
        running=False

print(h,m)

