import random
num= random.randrange(100,1000,2)
while True:
    a=int(input('enter a nuber:'))
    if a== num:
        print("congrates! you successfully gussed number",num)
        break
    elif a<num:
        print('enter greater number')
    elif a>num:
        print('enter smaller number')