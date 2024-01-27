a=[1,2,3,4,5,67867,7,8]
out=a[0]
out2=a[0]
for i in a:
    if out <i:
        out2=out
        out=i
    elif out2<i:
        out2=i
    
     
print(out,out2)