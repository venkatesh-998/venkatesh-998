def count(a,b):
    count=0
    for i in a:
        if i==b:
            count+=1
    return count
c=count('sdhfgrejk','a')
print(c)