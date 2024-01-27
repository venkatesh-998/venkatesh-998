import random
out=[]
while len(out)<6:
    out+=[str(random.randint(0,9))]
    out+=[chr(random.randint(65,90))]
    out+=[chr(random.randint(97,122))]
random.shuffle(out)
print(out)