#wap tofind gretest number of three digits
a=eval(input('enter the number:'))
b=eval(input('enter the numvber:'))
c=eval(input('enter the nuber:'))
if a>b and a>c:
    print('a is big value')
elif b>a and b>c:
    print('b is big value')
elif c>a and c>b :
    print('c is big value')
else:
    print('enter digit only')
if a==b:
    print('a and b are same values')
elif b==c:
    print('b and c are same values')
elif a==c:
    print('a and c are same values')
else:
    print('no same values')