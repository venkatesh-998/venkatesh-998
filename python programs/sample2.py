a=1233
b=236784
def sample():
    global a,b
    print(a) 
    print (b)
    def sample1():
        a=2356
        b=2563
        print(a)
        print(b)
        def sample2():
            a=4367
            print(a)
            print(b)
        sample2()
    sample1()
sample()
print(b)