import re
with open (r"C:\Users\administrator.MCA\Desktop\reet.txt.txt",'r',encoding='utf-8') as file:
    data=file.read()
    newdata=re.sub(' ','_',data)
    file.seek(0)
    file.write(newdata)