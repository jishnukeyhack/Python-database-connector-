import mysql.connector as con
#global variables
dbcon=con.connect(host='localhost',user='root', password='SHADLEY', database='shoes')
cur=dbcon.cursor()


#This function is used to generate the shoe code number automatically
def auto_icode():
    cmd="select * from shoes"
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        sc=101
    else:
        sc=record[len(record)-1][0]
        sc=sc+1
    return sc

#This function heloo
is used to generate bill number automatically
def auto_billno():
    cmd="select * from net_bill"
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        sc=1001
    else:
        sc=record[len(record)-1][0]
        sc=sc+1
    return sc
    

#This function is used to insert shoes record in the table "shoes"
def insert_record():
    while True:
        sc=auto_icode()
        print("shoe Code :",sc)
        snm=input("Enter shoe brand Name=")
        st=int(input("Enter the shoe stock="))
        pr=int(input("Enter the shoe price="))
        cmd="insert into shoes values({},'{}',{},{})".format(sc,snm,st,pr)
        cur.execute(cmd)
        dbcon.commit()
        ch=input("Add more Records(y/n):")
        if ch in "nN":
            break


#This function is used to show all records of the shoes table
def show_records():
    cmd="select * from shoes"
    cur.execute(cmd)
    record=cur.fetchall()
    for rec in record:
        print("---------------------------------------")
        print("shoe Code :",rec[0])
        print("shoe brand Name :",rec[1])
        print("Stock :",rec[2])
        print("Price :Rs",rec[3])
        print("---------------------------------------")


#This function is used to search details of the shoe w.r.t the shoe code
def search_record():
    sc=int(input("Enter the shoe code to search="))
    cmd="select * from shoes where mcode={}".format(sc)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("Invalid  Code")
    else:
        print("---------------------------------------")
        print("shoe Code :",record[0][0])
        print("shoe Name :",record[0][1])
        print("Stock :",record[0][2])
        print("Price :Rs",record[0][3])
        print("---------------------------------------")

#This function is used to update the stock of given shoe
def update_stock():
    sc=int(input("Enter the shoe code to update="))
    cmd="select * from shoe where scode={}".format(sc)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("Invalid shoe Code")
    else:
        stk=int(input("Enter the new stock value="))
        cmd="update shoe set stock=stock+{} where scode={}".format(stk,sc)
        cur.execute(cmd)
        dbcon.commit()
        print("Record Updated successfully")
        
        
#This function is used to delete a record from shoes table
def del_record():
    sc=int(input("Enter shoe code to delete="))
    cmd="select * from shoes where scode={}".format(sc)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("Invalid shoe Code")
    else:
        print("shoe Details to be deleted")
        print("---------------------------------------")
        print("shoe Code :",record[0][0])
        print("shoe Name :",record[0][1])
        print("Stock :",record[0][2])
        print("Price :Rs",record[0][3])
        print("---------------------------------------")
        cmd="delete from shoes where scode={}".format(sc)
        cur.execute(cmd)
        dbcon.commit()
        print("Record Deleted Successfully")
    
# This function is used to prepare the bill of the customer
def make_bill():
    billno=auto_billno()
    print("Bill Number=",billno)
    cnm=input("Enter Customer Name=")
    cont=input("Enter Contact Number =")
    s=0
    while True:
        sc=int(input("Enter the shoe code ="))
        cmd="select * from Medicine where scode={}".format(sc)
        cur.execute(cmd)
        record=cur.fetchall()
        if len(record)==0:
            print("Invalid shoe Code")
        else:
            print("shoe Name :",record[0][1])
            print("Price :Rs",record[0][3])
            snm=record[0][1]
            pr=record[0][3]
            qty=int(input("Enter the Quantity:"))
            amt=pr*qty
            print("Amount =Rs",amt)
            s=s+amt
            cmd="update shoes set stock=stock-{} where scode={}".format(qty,sc)
            cur.execute(cmd)
            dbcon.commit()
            cmd="insert into shoes_bill values({},{},'{}',{},{},{})".format(billno,scode,snm,pr,qty,amt)
            cur.execute(cmd)
            dbcon.commit()
        x=input("Add More shoes (y/n):")
        if x in "nN":
            break
    print("Total Bill=Rs",s)
    disc=s*10/100
    net=s-disc
    print("Discount :Rs",disc)
    print("Net Bill=Rs",net)
    cmd="insert into net_bill values({},'{}','{}',{},{},{})".format(billno,cnm,cont,s,Disc,net)
    
    cur.execute(cmd)
    dbcon.commit()

def search_bill():
    billno=int(input("Enter the bill number to search="))
    cmd="select * from net_bill where bno={}".format(billno)
    cur.execute(cmd)
    record=cur.fetchall()
    if len(record)==0:
        print("Invalid Bill number")
    else:
        cmd="select * from shoes_bill where bno={}".format(billno)
        cur.execute(cmd)
        record1=cur.fetchall()
        print("Customer Name :",record[0][1])
        print("Contact Number :",record[0][2])
        print("\n======================================")
        for rec in record1:
            print("shoe Name : ",rec[2],"\t Qty : ",rec[3],"\tPrice: Rs",rec[4],"\tAmount:Rs",rec[5])
        print("\n=======================================")
        print("Total Amount :Rs",record[0][3])
        print("Discount Amount :Rs",record[0][4])
        print("Net Amount :Rs",record[0][5])
    
        
           
    
    
    
#----------Main Section-------
if dbcon.is_connected():
    while True:
        print(''' Menu\n1)Add shoes\n2) Show all shoes
              \n3) Search shoe brand\n4)Update Stock
              \n5) Remove shoe\n6)Make Bill
              \n7) Search Bill\n8)Exit''')
        ch=int(input("Enter the choice="))
        if ch==1:
            insert_record()
        elif ch==2:
            show_records()
        elif ch==3:
            search_record()
        elif ch==4:
            update_stock()
        elif ch==5:
            del_record()
        elif ch==6:
            make_bill()
        elif ch==7:
            search_bill()
        elif ch==8:
            break
                             
        x=input("Goto Main Menu(y/n):")
        if x in "nN":
            break
    
else:
    print("Connection failure")
      
