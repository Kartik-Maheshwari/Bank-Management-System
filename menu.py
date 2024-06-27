import datetime as dt
import random
import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='141974',database='bank')
cur = conn.cursor()
conn.autocommit = True
c = 'y'
while c == 'y':
        print()
        print('1.CREATE NEW BANK ACCOUNT')
        print()
        print('2.TRANSACTION')
        print()
        print('3.CUSTOMER DETAILS')
        print()
        print('4.TRANSACTION DETAILS')
        print()
        print('5.DELETE ACCOUNT')
        print()
        print('6.QUIT')

        print()
        n=int(input('Enter your CHOICE='))
        print()

        if n == 1:
                acc_no= int(11110000 + random.randint(0,9999))
                print('Your ACCOUNT NUMBER is ("Please note it down"):',acc_no)
                print()
                acc_name=input('Enter your ACCOUNT NAME=')
                print()
                ph_no=int(input('Enter your PHONE NUMBER='))
                print()
                add=(input('Enter your place='))
                print()
                cr_amt=int(input('Enter your credit amount='))
        
                SQLInsert="INSERT  INTO customer_details values ({},'{}','{}','{}','{}')".format(str(acc_no),acc_name,str(ph_no),add,str(cr_amt))
                cur.execute(SQLInsert)
                print()
                print('Account Created Succesfully!!!!!')
                conn.commit()
    

        if n == 2:
            acct_no=int(input('Enter Your Account Number='))
            cur.execute('select * from customer_details where acct_no={}'.format(str(acct_no)))
            data=cur.fetchall()
            count=cur.rowcount
            conn.commit()
            if count == 0:
                print()
                print('Account Number Invalid Sorry Try Again Later')
                print()
            else:
                print()
                print('1.WITHDRAW AMOUNT')
                print()
                print('2.ADD AMOUNT')
                print()
                print('PRESS ANY  OTHER KEY TO GO BACK')
                print()

                print()
                x=int(input('Enter your CHOICE='))
                print()
                if x == 1:
                        amt=int(input('Enter withdrawl amount='))
                        cr_amt=0
                        cur.execute('update customer_details set  cr_amt=cr_amt- {} where acct_no= {}'.format(str(amt),str(acct_no)))
                        SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),amt,cr_amt) 
                        cur.execute(SQLInsert)
                        conn.commit()
                        print()
                        print('Ammout Withdrawn Succesfully!!!!!')
                                        
                if x== 2:
                        amt=int(input('Enter amount to be added='))
                        cr_amt=0
                        cur.execute('update customer_details set  cr_amt=cr_amt+ {} where acct_no= {}'.format(str(amt),str(acct_no)))
                        SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),cr_amt,amt)
                        cur.execute(SQLInsert)
                        conn.commit()
                        print()
                        print('Amount Added Succesfully!!!!!')

        if n == 3:
                acct_no=int(input('Enter your account number='))
                print()
                cur.execute('select * from customer_details where acct_no= {}'.format(str(acct_no)))
                if cur.fetchone() is  None:
                        print()
                        print('Invalid Account number')
                else:
                        cur.execute('select * from customer_details where acct_no= {}'.format(str(acct_no)))
                        data=cur.fetchall()
                        for row in data:
                             print('ACCOUNT NO=',acct_no)
                             print()
                             print('ACCOUNT NAME=',row[1])
                             print()
                             print(' PHONE NUMBER=',row[2])
                             print()
                             print('ADDRESS=',row[3])
                             print()
                             print('cr_amt=',row[4])
        if n == 4:
                acct_no=int(input('Enter your account number='))
                print()
                cur.execute('select * from customer_details where acct_no= {}'.format(str(acct_no)))
                if cur.fetchone() is  None:
                        print()
                        print('Invalid Account number')
                else:
                        cur.execute('select * from transactions where acct_no= {}'.format(str(acct_no)))
                        data=cur.fetchall()
                        for row in data:
                            print('ACCOUNT NO=',acct_no)
                            print()
                            print('DATE=',row[1])
                            print()
                            print(' WITHDRAWAL AMOUNT=',row[2])
                            print()
                            print('AMOUNT ADDED=',row[3])
                            print()
                               
        if n == 5:
                print('DELETE YOUR ACCOUNT')
                acct_no=int(input('Enter your account number='))
                              
                cur.execute('delete from customer_details where acct_no= {}'.format(str(acct_no)))
                print('ACCOUNT DELETED SUCCESFULLY')

        if n == 6:
                print('DO YO WANT TO CONTINUE(y/n)')
                c=input('enter your choice=')
else:
     print('THANK YOU PLEASE VISIT AGAIN')
     quit()
     
    
                               
                              
                              
                              

                                        
               
     


