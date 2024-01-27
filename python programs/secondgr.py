a=eval(input('enter the number:'))
b=eval(input('enter the numvber:'))
c=eval(input('enter the nuber:'))
if a>b and a>c:
    if b>c :
        print('b is second greatest')
    else:
        print('c is second greatest ')
elif b>c:
    if a>c:
      print('ais second greatest')
    else:
      print('c is second greatest')
else:
    if a>b:
      print ('ais second greatest')
    else:
      print('bis second greatest')  
      

