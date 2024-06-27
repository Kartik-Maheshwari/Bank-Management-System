import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='141974',database='bank')
cur = conn.cursor()
cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null )')
