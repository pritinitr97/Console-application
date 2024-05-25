from os import *
import sys
from colorama import *
import pymysql
def by_rollno():
    n=int(input("Enter the rollno :"))
    con=pymysql.connect(host='localhost',user='root',password='Abl@721101',db='college',autocommit=True)
    cur=con.cursor()
    q="select * from student where rno=%s"
    val=(n,)
    cur.execute(q,val)
    row=cur.fetchone()
    if row==None:
        print(Back.RED+Fore.YELLOW+" "*44+"Not found")
    else:
        print("Student Record")
        print('-'*40)
        print(" Student's Rollno     :",row[0])
        print(" Student's Name       :",row[1])
        print("Father Name           :",row[2])
        print("Gender                :",row[3])
        print("Dob                   :",row[4])
        print("Address               :",row[5])
        print("Phone no              :",row[6])
        print("Course                :",row[7])
        print("Section               :",row[8])
        system('pause')
def by_name():
    n=input("Enter the name :")
    con=pymysql.connect(host='localhost',user='root',password='Abl@721101',db='college',autocommit=True)
    cur=con.cursor()
    q="select * from student where name=%s"
    val=(n,)
    cur.execute(q,val)
    row=cur.fetchone()
    if row==None:
        print(Back.GREEN+Fore.YELLOW+" "*44+"Not found")
    else:
        print("Student Record")
        print('-'*40)
        print(" Student's Rollno     :",row[0])
        print(" Student's Name       :",row[1])
        print("Father Name           :",row[2])
        print("Gender                :",row[3])
        print("Dob                   :",row[4])
        print("Address               :",row[5])
        print("Phone no              :",row[6])
        print("Course                :",row[7])
        print("Section               :",row[8])
        system('pause')
def by_course():
    n=input("Enter the course name :")
    con=pymysql.connect(host='localhost',user='root',password='Abl@721101',db='college',autocommit=True)
    cur=con.cursor()
    q="select * from student where course=%s"
    val=(n,)
    cur.execute(q,val)
    row=cur.fetchone()
    if row==None:
        print(Back.RED+Fore.YELLOW+" "*44+"Not found")
    else:
        print("Student Record")
        print('-'*40)
        print(" Student's Rollno     :",row[0])
        print(" Student's Name       :",row[1])
        print("Father Name           :",row[2])
        print("Gender                :",row[3])
        print("Dob                   :",row[4])
        print("Address               :",row[5])
        print("Phone no              :",row[6])
        print("Course                :",row[7])
        print("Section               :",row[8])
        system('pause')
    
    

def search_menu():
    while(True):
        system ('color 2f')
        system('cls')
        print('\n'*5)
        print(Back.GREEN+Fore.RED+" "*46+"SUDENT SEARCH MENU")
        print(Back.GREEN+Fore.RED+" "*40+"------------------------")
        print(Back.GREEN+Fore.BLUE+" "*44+"1 Search by rollno")
        print(Back.GREEN+Fore.BLUE+" "*44+"2 Search by name")
        print(Back.GREEN+Fore.BLUE+" "*44+"3 Search by course")
        print(Back.GREEN+Fore.BLUE+" "*44+"4 Back to student menu")
        print(Back.GREEN+Fore.RED+" "*40+"-------------------------")
        choise=int(input(Back.GREEN+Fore.BLUE+" "*44+"Enter your Choise: "))
        if choise==1:
            by_rollno()
        elif choise==2:
            by_name()
        elif choise==3:
            by_course()
        elif choise==4:
            return

