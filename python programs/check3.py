a = input('enter the password')
val={
  'upper':False,
  'lower':False,
  'num':False,
  'char':False,
  'space':True
}
if len(a):
  for char in a:
    if ( 'A'<=char<='Z'):
      val['upper']=True
    elif'a'<=char<='z' :
      val['lower']=True
    elif '0' <=char <='9':
      val['num']=True
    elif char!=' ':
      val['char']=' '
    elif char==' ':
      val['space']=True
if val['upper'] and val['lower']and val['num']and val['char']and val['char']:
    print('valid pass word')
else:
  print('not valid')  


      