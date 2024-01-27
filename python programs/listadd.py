a=[1,9,11,23,65,78,43,2]
b=len(a)
sum = 0
prod = 1
if b%2==0:
    for i in a:
        sum=sum+i
    print(sum)
else:
    for i in a:
        prod=prod*i
    print(prod)
