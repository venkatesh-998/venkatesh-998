import csv
#with open('sample2.csv','w',newline='') as csvfile:
    #fieldnames=['id','name','age']
    #record=csv.DictWriter(csvfile,fieldnames)
    #record.writeheader()
    #data=[
         #{'id':1,'name':'ramanareddy','age':27},
         #{'id':2,'name':'lekha','age':25},
   # ]
    #record.writerows(data)

with open('sample2.csv','r',newline='')as file:
    records=csv.DictReader(file)
    for i in records:
        print(i)