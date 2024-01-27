out=1
for i in range(1,11):
    out=1
    for j in range(1,i+1):
        out*=j
    print('factorial of',i,':',out)
    