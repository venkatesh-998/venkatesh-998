opd1=int(input('enter the number'))
opd2=int(input('enter the number'))
operator=eval(input('enter the operator'))
match operator:
    case '+':
       print(opd1+opd2)
    case '-':
        print(opd1-opd2)
    case'*':
        print(opd1*opd2)
    case '/':
        print(opd1/opd2)
    case _:
        print('invalid operator')

