def index(a):
    out=[]
    i=0
    while i<len(a):
        if a[i] in 'a,e,i,o,u,A,E,I,O,U':
            out=out+[i]
        i+=1
    return out
out=index('hello world')
print(out)