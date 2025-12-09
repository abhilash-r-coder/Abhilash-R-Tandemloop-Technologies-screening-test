x=int(input('enter a number :'))
l=[]
n=1
if x%2==0:
    x=x-1

while len(l)!=x:
    if n%2!=0:
        l.append(n)
    n+=1
print(l)