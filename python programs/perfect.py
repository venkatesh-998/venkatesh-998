out=0
a=int(input('enter the number'))
for i in range(1,a):
    if a%i==0:
        out=out+int(i)
if out==a:
    print('it is a perfect number')
else:
    print('not perfect')
