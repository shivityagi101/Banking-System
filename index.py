import random
import mysql.connector as m1
con=m1.connect(host="localhost",database="its10",user='root',password='itskills')
if con.is_connected():
    def openAcno():
        a=random.randint(1,9)
        b = random.randint(1, 9)
        c = random.randint(1, 9)
        d = random.randint(1, 9)
        acno="HDFC"+str(a)+str(b)+str(c)+str(d)
        return acno

    def validateAcc(acno):
        qry="select * from bank where acno='{}'".format(acno)
        cursor=con.cursor()
        cursor.execute(qry)
        rows=cursor.fetchone()
        if rows=="":
            return False
        else:
            return True
            

    def genAcc():
        balance=0
        acno=openAcno()
        print("Your account number is: ",acno)
        name=input("Enter your name: ")
        actype=input("Enter your account type: ")
        if actype=="saving":
            balance=1000
        elif actype=="current":
            balance=2000
        else:
            balance=3000
        print("Your balance is: ",balance)
        qry="insert into bank values('{}','{}','{}','{}')".format(acno,name,actype,balance)
        cursor=con.cursor()
        cursor.execute(qry)
        con.commit()
        con.close()

    def deposit():
        amt=int(input("Enter amount to be deposited: "))
        if amt>0:
            acno=input("Enter account number: ")
            qry = "select * from bank where acno ='{}'".format(acno)
            cursor = con.cursor()
            cursor.execute(qry)
            rows = cursor.fetchone()
            if cursor.rowcount == 0:
                print("Data not found")
            else:
                newbal=rows[3]+amt
                qry="update bank set balance={} where acno='{}'".format(newbal,acno)
                cursor = con.cursor()
                cursor.execute(qry)
                con.commit()
                con.close()
                print("Deposited successfully!")
        else:
            print("Invalid amount!")

    def withdraw():
        acno=input("Enter account number: ")
        amt=int(input("Enter amount to be withdraw: "))
        qry="select * from bank where acno='{}'".format(acno)
        cur=con.cursor()
        cur.execute(qry)
        rows=cur.fetchone()
        if amt<rows[3]:
            newbal=rows[3]-amt
            qry="update bank set balance={} where acno='{}'".format(newbal,acno)
            cursor = con.cursor()
            cursor.execute(qry)
            con.commit()
            con.close()
            print("withdrew successfully!")
        else:
            print("Insufficient funds!")

    def transfer():
        acno1 = input("Enter account number from which money be withdrawn:")
        acno2 = input("Enter account number to which money should be deposited:")
        amt=int(input("Enter amount: "))
        qry="select * from bank where acno='{}'".format(acno1)
        cur=con.cursor()
        cur.execute(qry)
        rows=cur.fetchone()
        if amt<rows[3]:
            newbal=rows[3]-amt
            qry="update bank set balance={} where acno='{}'".format(newbal,acno1)
            cur.execute(qry)
            con.commit()
        else:
            print("Insufficient funds!")
        qry="select * from bank where acno='{}'".format(acno2)
        cur.execute(qry)
        rows=cur.fetchone()
        newbal1=rows[3]+amt
        qry="update bank set balance={} where acno='{}'".format(newbal1,acno2)
        print("Money transfered!")
        cur=con.cursor()
        cur.execute(qry)
        con.commit()
        con.close()

    def display():
        qry="select * from bank"
        cur=con.cursor()
        cur.execute(qry)
        rows=cur.fetchall()
        for x in rows:
            print("Account number is: ",x[0])
            print("name is: ",x[1])
            print("Account type is: ",x[2])
            print("Balance is: ",x[3])
            print("="*50)

    def close():
        acno=input("Enter account number: ")
        qry="delete from bank where acno='{}' ".format(acno)
        cur=con.cursor()
        cur.execute(qry)
        con.commit()
        con.close()
        print("Record delete successfully!")

    k=""
    while True:
        print('''
        Main menu:
        1.open account:
        2.deposit money:
        3.withdraw money:
        4.transfer money:
        5.display all:
        6.close account:
        7.exit:
        ''')
        
        choice=int(input("Enter your choice: "))
        match choice:
            case 1:
                genAcc()
            case 2:
                deposit()
            case 3:
                withdraw()
            case 4:
                transfer()
            case 5:
                display()
            case 6:
                close()
            case 7:
                quit()
    
        k=input("Do you want to continue?... Enter Yes to continue: ")
        if k in ['no','NO','No','nO']:
            break
