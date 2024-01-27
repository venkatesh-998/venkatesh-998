a=int(input('enetr the number'))
i=1
count=0
while i<=a:
    if a%i==0:
        count+=1
    i+=1
if count==2:
     print('prime')
else:
     print('not prime')