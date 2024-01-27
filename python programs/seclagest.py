a=[12,234,566,234,3467]
out=a[0]
for i in a:
    if out<i and i!=out:
        out=i
print(out)