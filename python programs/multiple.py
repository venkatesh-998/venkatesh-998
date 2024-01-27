def multiple(i):
        if i%3==0:
            return True
        else :
            return False
out=filter(multiple,range(1,200))
print(list(out))
        
