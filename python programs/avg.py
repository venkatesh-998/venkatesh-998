def listavg(a):
    for i in a:
        if len(i)%2==0:
            yield (i[0]+i[-1])/2
        else:
            yield i[len(i)//2]
a=[(1,2),[1,2,3,4],(12,34,567)]
out =listavg(a)
print(list(out))