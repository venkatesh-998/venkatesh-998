seats=int(input('enter the seats'))
option=int(input('select the option'))
match option:
    case 1:
        print("dimond class")
        amt=seats*200
    case 2:
        print('golden class')
        amt=seats*150
    case 3:
        print('silverclass')
        amt=seats*100
    case _:
        print("invalid option")
print(amt)

