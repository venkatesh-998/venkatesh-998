def check(a):
    for i in a:
        if type(i)==int or type(i)==float or type(i)==bool:
            yield i
        else:
            yield len(i)
b=[1,[4,5,6],{7,8},'efg',{'a':1},9.]
c=check(b)
print(list(c))