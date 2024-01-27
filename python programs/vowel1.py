def string(a):
    out=[]
    for i in range(0,len(a)):
        if a[i] in 'a,e,i,o,u,A,E,I,O,U':
            out+=[i]
    return out
b=string('hello world')
print(b)