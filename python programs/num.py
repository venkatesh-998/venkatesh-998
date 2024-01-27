def 
a= eval(input('enter the word'))
i=0
while i<len(a):
    if a[i] in '1,2,3,4,5,6,7,8,9,0':
        count+=1
        print (a[i])
    i+=1
