def fname(a):
    if a%2==0:
        return True
    else:
        return False
out=filter(fname,[1,1,1,2,3,3,4,4,4,6])
print(list(out))