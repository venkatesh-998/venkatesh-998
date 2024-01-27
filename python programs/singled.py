def single(i):
    if type(i)==int or type(i)==bool or type(i)==float or type(i)==complex:
        return True
    else:
        return False
out=filter(single,['sa',1,(1,23),{'s':1},2.9,3.9])
print(list(out))
           