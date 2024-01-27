import pymysql
import csv
conn=pymysql.Connection(user='root',password='root',host='localhost',port=3306,db='mca11')
cur=conn.cursor()

def createtable():
    query='''create table vegitables(
    id int(2) primary key,
    nameofitems varchar(20)
    );
    '''
    cur.execute(query)

def insert(sid,name):
    record=(sid,name)
    query='''insert into vegitables(id,nameofitems) values (%s,%s)'''
    cur.execute(query,record)
    conn.commit()

def read_records():
    query='select*from vegitables'
    cur.execute(query)
    record=cur.fetchall()
    for row in record:
        print(row)
    #with open('records.csv','w') as csvfile:
       ##data.writerow(['id','nameofitems'])
    #for row in record:
        #data.writerow(row)
       # print(row)


def update_record(sid,name):
    record=[sid,name]
    cur.execute('update vegitables set nameofitems=(%s) where id=(%s)',record)
    conn.commit()

def fetch_record(sid):

    query='select *from vegitables where id=%s'
    cur.execute(query,sid)
    record=cur.fetchall()
    for row in record:
        print(row)


def update_name(sid):
    fetch_record(sid)
    name=input('enter new name to update..:-')
    record=[name,sid]
    query ='update vegitables set nameofitems=%s where id=%s'
    cur.execute(query,record)
    conn.commit()
    fetch_record(sid)

def delete_records(sid):
    record=[sid]
   # query='delete from vegitables'
    cur.execute('delete from vegitables where id=%s',record)
    conn.commit()


def truncate():
    query='truncate table vegitables'
    cur.execute(query)

def insert_recsv():
    with open('records.csv','r') as csvfile:
        data=csv.reader(csvfile)
        data=list(data)
        for row in range(1,len(data)):
            insert(*data[row])