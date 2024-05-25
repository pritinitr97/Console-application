from os import *
import sys
from colorama import *
from pwinput import *
import pymysql
import time
from tqdm import *


def display_marksheet():
    system('color 3f')
    system('cls')
    print('\n'*10)
    n=int(input(' '*45+"enter the roll no: "))
    con=pymysql.connect(host='localhost',user='root',password='Abl@721101',db='college',autocommit=True)
    cur=con.cursor()
    q="select * from student,marks where student.rno=marks.rno and marks.rno=%s"
    val=(n,)
    cur.execute(q,val)
    row=cur.fetchone()
    if row==None:
        print(' '*45+"not found")
        system('pause')
    else:
        system('color 3f')
        system('cls')
        print('\n'*5)
        print(' '*40+Fore.BLUE+"MIDNAPORE CITY COLLEGE")
        print(' '*40+Fore.BLUE+"      MIDNAPORE     ")
        print()
        print(' '*40+Fore.RED+"  M A R K S H E E T ")
        print(' '*40+Fore.RED+"----------------------")
        print()
        print(' '*10+Fore.BLUE+"Roll no       :",row[0],' '*50,"Course/Class:",row[7])
        print(' '*10+Fore.BLUE+"Name          :",row[1],' '*48,"Section     :",row[8])
        print(' '*10+Fore.BLUE+"Father's Name :",row[2],' '*45,"DOB         :",row[4])
        print('-'*110)
        print(Fore.WHITE+"%10s %20s %20s %20s %20s"%("sno","subject","max marks","marks obtatned","grade"))
        print('-'*110)
        if row[15]>=80:
            g='A'
        elif row[15]>=60:
            g='B'
        elif row[15]>=40:
            g='C'
        else:
            g='F'
        print(Fore.WHITE+"%10s %20s %20s %20s %20s"%(1,row[10],100,row[15],g))
        if row[16]>=80:
            g='A'
        elif row[16]>=60:
            g='B'
        elif row[16]>=40:
            g='C'
        else:
            g='F'
        print(Fore.WHITE+"%10s %20s %20s %20s %20s"%(2,row[11],100,row[16],g))
        if row[17]>=80:
            g='A'
        elif row[17]>=60:
            g='B'
        elif row[17]>=40:
            g='C'
        else:
            g='F'
        print(Fore.WHITE+"%10s %20s %20s %20s %20s"%(3,row[12],100,row[17],g))
        if row[18]>=80:
            g='A'
        elif row[18]>=60:
            g='B'
        elif row[18]>=40:
            g='C'
        else:
            g='F'
        print(Fore.WHITE+"%10s %20s %20s %20s %20s"%(4,row[13],100,row[18],g))
        if row[19]>=80:
            g='A'
        elif row[19]>=60:
            g='B'
        elif row[19]>=40:
            g='C'
        else:
            g='F'
        print(Fore.WHITE+"%10s %20s %20s %20s %20s"%(5,row[14],100,row[19],g))
        print('-'*110)
        print(' '*45+Fore.GREEN+"Total marks:",row[20])
        print(' '*45+Fore.GREEN+"Percentage:",row[21])
        print(' '*45+Fore.GREEN+"Grade:",row[22])
        system('pause')

def change_password():
    system('color 6f')
    system('cls')
    print('\n'*10)
    print(' '*45+Fore.WHITE+"CHANGE PASSWORD:")
    print(' '*42+Fore.WHITE+"------------------")
    print()
    current=input(' '*30+Fore.WHITE+"Enter the current password:")
    con=pymysql.connect(host='localhost',user='root',password='Abl@721101',db='college')
    cur=con.cursor()
    q="select * from admin where password=%s"
    val=(current,)
    cur.execute(q,val)
    row=cur.fetchone()
    if row==None:
        print(' '*45+"Incorrect")
    else:
        print()
        new=input(' '*30+Fore.WHITE+"Enter the new password:")
        
        q="update admin set password=%s"
        val=(new,)
        cur.execute(q,val)
    
        print(' '*30+Fore.WHITE+"Successfully Updated")
        system('pause')
    
    
    
            

while True:
    system ('color 4f')
    system('cls')
    print('\n'*10)
    uname=input(Fore.BLACK+" "*45+"Enter the USER NAME:")
    pa=pwinput(prompt=" "*45+"Enter the PASSWORD:",mask='*')
    con=pymysql.connect(host='localhost',user='root',password='Abl@721101',db='college')
    cur=con.cursor()
    q="select * from admin where name=%s and password=%s"
    val=(uname,pa)
    cur.execute(q,val)
    row=cur.fetchone()
    if row==None:
        print()
        print(Fore.WHITE+" "*45+"Incorrect user name or password")
        choise=input(" "*45+'Try again y/n ?')
        if choise in 'yY':
            continue
        else:sys.exit()
    else:
        con.close()
        break
   
    

system('color 6f')
system('cls')
print('\n'*3)
print(Fore.CYAN+' '*45+"S T U D E N T  M A N A G M E N T")
print()
print(Fore.CYAN+' '*45+"             &")
print()
print(Fore.CYAN+' '*50+"M A R K S H E E T")
print()
print()
print()

for i in tqdm (range (20),desc="Plese wait"):
    time.sleep(0.3)
   

system(' color 4f')
system('cls')
print('\n'*3)
print(Back.RED+Fore.YELLOW+" "*45+"M A I N  M E N U")
print(Back.RED+Fore.YELLOW+" "*44+"------------------")
print(Back.RED+Fore.GREEN+" "*44+"1 Student Menu")
print(Back.RED+Fore.GREEN+" "*44+"2 Marks entry Menu")
print(Back.RED+Fore.GREEN+" "*44+"3 Marksheet")
print(Back.RED+Fore.GREEN+" "*44+"4 Change Password")
print(Back.RED+Fore.GREEN+" "*44+"5 Exit")
print(Back.RED+Fore.GREEN+" "*44+"------------------")
choise=int(input(Back.RED+Fore.WHITE+" "*44+"Enter Your Choise ?"))



if choise==1:
    import student
    student.student_menu()
elif choise==2:
    import marks
    marks.marks_menu()
elif choise==3:
    display_marksheet()
elif choise==4:
    change_password()
elif choise==5:
    print("Exit")
    

