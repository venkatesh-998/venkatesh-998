a=int(input('enter the number'))
count=0
for i in range(2,a):
    if a%i==0:
        count+=1
    i+=1
if count==0:
    print('prime')
else:
    print('not prime')