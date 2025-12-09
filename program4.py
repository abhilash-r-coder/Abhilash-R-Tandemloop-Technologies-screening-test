
l=[1,2,8,9,12,46,76,82,15,20,30]

d={
    i:sum(1 for x in l if x%i==0)
    for i in range(1,10)
}
print(d)