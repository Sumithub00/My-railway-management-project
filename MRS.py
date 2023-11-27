# connect Database 
import mysql.connector as a
con=a.connect(host="localhost",user="root",passwd='root')
 
# Select Data Base If Exist 
 
c=con.cursor()
c.execute("Show databases")
dl=c.fetchall()
dl2=[ ]
for i in dl:
   dl2.append(i[0])
if 'myrailway' in dl2:
   sql="use myrailway"
   c.execute(sql)
else:
   sql1="create database myrailway"
   c.execute(sql1)
   sql2="use myrailway"
   c.execute(sql2)
   sql3="create table Train(Name varchar(50),cost integer,Distance integer,Data varchar(20))"
   c.execute(sql3)
   sql4="create table customer(Name varchar(20),Train varchar(25),Payment integer,Data varchar(20),Phone varchar(20))"
   c.execute(sql4)
   sql5="create table Bills (Details varchar(20),Cost integer,Data varchar(20))"
   c.execute(sql5)
   sql6="create table worker(Name varchar(50),work varchar(15),Salary varchar(20))"
   c.execute(sql6)
   con.commit()
 	
# system password login
def signin():
   print("\n")
   print("--------------->>>>>>>>>>Welcome,My"     
    "Railway Management System To My All [MRMSTMA]<<<<<<<<<--------")
   p=input("Enter the system password:")
   if p=="mrs456":
    	options()
   else:
    	signin()
    	
# options fuction
def  options():
   print("""  
                     1.Add Train
    		         2.Book Train
    		         3.Add Bill
    		         4.Add worker
    		         5.Display Train
    		         6.Display payments
    		         7.Display Bills 
    		         8.Display Worker    """)
   choice=input("select option:")
   while True:
    	if (choice=='1'):
    		AddTrain()
    	elif (choice=='2'):
    		BookTrain()
    	elif (choice=='3'):
    		AddBills()
    	elif (choice=='4'):
    		Addworker()
    	elif (choice=='5'):
    		DisplayTrain()
    	elif (choice=='6'):
    		DisplayPayments()
    	elif (choice=="7"):
    		DisplayBills()
    	elif (choice=="8"):
    		DisplayWorker()
    	else:
    		print("Enter Again")
    		options()
    				
# Function to add new trains data into train table 
def AddTrain():
    		n=input("Train name:")
    		c=input("cost:")
    		b=input("Distance:")
    		d=input("Date:")
    		data=(n,c,b,d)
    		sql='insert into Train values(%s,%s,%s,%s)'
    		c=con.cursor()
    		c.execute(sql,data)
    		con.commit()
    		print("Data inserted successfully")
    		options()
    		 
#function to display data from Train table
def DisplayTrain():
	sql='select * from Train'
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d:
		print("Name:", i[0])
		print("Cost:", i[1])
		print("Distance:", i[2])
		print("Date:", i[3])
		print("---------")
	options()
	
	
# fuction to book Train data into Train table
def BookTrain():
	n=input("Customer name:")
	s=input("Train:")
	py=int(input("Payment:"))
	d=input("Date:")
	p=input("phone:")
	data=(n,s,py,d,p)
	sql='insert into customer values(%s,%s,%s,%s,%s)'
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inserted successfully")
	options()
	
	
# function to display payment data from the customer table
def DisplayPayments():
	sql='select * from customer'
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d:
	     print("Name:", i[0])
	     print("Train:", i[1])
	     print("Payment:", i[2])
	     print("Date:", i[3])
	     print("phone:", i[4])
	     print("-----------")
	options()
		
		
# fucntion  to add new bills
def AddBills():
	dt=input("Details:")
	c=input("Cost:")
	d=input("Date:")
	data=(dt,c,d)
	sql='insert into Bills values(%s,%s,%s)'
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inserted successfully")
	options()
	
	
#fuction to display all bills
def DisplayBills():
	sql='select * from Bills'
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d:
		print("Detail:",i[0])
		print("Cost:",i[1])
		print("Date:",i[2])
		print("-----------")
	options()
 
# function to add new worker 
def Addworker():
	n=input("Name:")
	w=input("work")
	s=input("salary")
	data=(n,w,s)
	sql='insert into worker values(%s,%s,%s)'
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inserted successfully")
	options()
	
# fuction to dislpay all worker
def DisplayWorker():
	sql='select *from worker'
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for  i in d:
		print("Name:",i[0])
		print("work:",i[1])
		print("salary:",i[2])
		print("---------")
	options()
	
signin()
