p=int(input('enter the number'))
for i in range(p):
    for j in range(p):
        if i==j or i==p-j-1:
            print(' ',end='')
        else:
            print('* ',end='')
    print()