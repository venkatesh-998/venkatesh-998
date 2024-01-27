a=input('enter the word')
i=0
count=0
while i<len(a):
    if a[i] in 'a,e,i.o,u,A,E,I,O,U':
        count+=1
    i+=1
print(count)