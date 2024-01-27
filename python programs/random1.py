import random
out =''
for i in range(10):
    if len(out)<4:
        out+=str(random.randint(0,9))
print(out)