import pymysql
import aws_credentials as rds
conn = pymysql.connect(
        host= 'regis.c0frqei3jmlg.ap-south-1.rds.amazonaws.com',
        port = 3306,
        user = 'admin',
        password = 'akanksha1110',
        db = 'registration'
        )


def insert_details(name,email,phone,passwd, cpasswd):
    cur=conn.cursor()
    cur.execute("INSERT INTO user(name,email,phone,passwd, cpasswd) VALUES (%s,%s,%s,%s,%s)", (name,email,phone,passwd, cpasswd))
    conn.commit()

def get_details(name, passwd):
    cur=conn.cursor()
    cur.execute('SELECT name, passwd FROM user WHERE name = %s AND passwd = %s', (name, passwd,))
    account = cur.fetchone()
    
    return account
            
