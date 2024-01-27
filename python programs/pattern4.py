p=int(input('enter the number'))
temp=p//2
out=''
for i in range(p):
    for j in range(p):
        if i in [0,p-1,] or j in [0,p-1]:
            out+='* '
        else:
            out+=' '
        out+='\n'
print(out)
