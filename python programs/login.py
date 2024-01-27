
person ={'username':'bhaskar','password':'1234567890'}
a=eval(input('enter the username'))
b=eval( input('enter password'))
if a == person['username'] and b == person['password']:
    print('your successfully login your account')
else:
    print('plese enter valid  username')