from os import *
import sys
from colorama import *
import pymysql
def add_student():
    system ('color 6f')
    system('cls')
    print('\n'*5)
    print(Back.YELLOW+Fore.BLUE+" "*44+" Add new Student")
    print(Back.YELLOW+Fore.BLUE+" "*42+"--------------------")
    try:

            
        trno=int(input("Enter the roll no:"))
        tname=input("Enter the name:")
        tfname=input("Enter the father name:")
        tgen=input("Enter the gender:")
        print("Enter the dob:")
        d=input("Day:")
        m=input("month:")
        y=input("year:")
        tdob=y+'-'+m+'-'+d
        tadd=input("Enter address:")
        tphone=int(input("Enter the phone no:"))
        tcourse=input("Enter the course:")
        tsection=input("Enter the section:")
        con=pymysql.connect(host='localhost',user='root',password='Abl@721101',db='college',autocommit=True)
        cur=con.cursor()
        q="insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(trno,tname,tfname,tgen,tdob,tadd,tphone,tcourse,tsection)
        cur.execute(q,val)
        con.close()
        print("successfull saved .............................")
    except:
        print("Duplicate roll no or Invalid data are inputted")
def delete_student():
    system ('color 4f')
    system('cls')
    print('\n'*5)
    print(Back.RED+Fore.YELLOW+" "*44+" Delete Student Record")
    print(Back.RED+Fore.YELLOW+" "*42+"---------------------------")
    n=int(input("Enter the roll no:"))
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
        ch=input("Delete it y/n ?")
        if ch in 'yY':
            q="delete from student where rno=%s"
            cur.execute(q,val)
            print("Successfully Deleted")

def list_student():
    system ('color 4f')
    system('cls')
    print('\n'*5)
    print(Back.RED+Fore.YELLOW+" "*60+" List of student")
    print(Back.RED+Fore.YELLOW+" "*50+"-----------------------------------------------")
    print(Back.RED+Fore.YELLOW+"%20s %20s %20s %20s %20s %20s"%("RNO","NAME","FNAME","PHONE","COURSE","SECTION"))
    print('-'*150)
    con=pymysql.connect(host='localhost',user='root',password='Abl@721101',db='college',autocommit=True)
    cur=con.cursor()
    q="select * from student "
    cur.execute(q)
    for row in cur:
        print(Back.RED+Fore.YELLOW+"%20s %20s %20s %20s %20s %20s"%(row[0],row[1],row[2],row[6],row[7],row[8]))
        
        system('pause')

    
    
def student_menu():
  system ('color 2f')
  system('cls')
  print('\n'*5)
  print(Back.GREEN+Fore.RED+" "*46+"SUDENT MENU")
  print(Back.GREEN+Fore.RED+" "*42+"------------------")
  print(Back.GREEN+Fore.BLUE+" "*44+"1 add New Studet")
  print(Back.GREEN+Fore.BLUE+" "*44+"2 Delete Student record")
  print(Back.GREEN+Fore.BLUE+" "*44+"3 Search Student")
  print(Back.GREEN+Fore.BLUE+" "*44+"4 List of Students")
  print(Back.GREEN+Fore.RED+" "*42+"-----------------------")
  choise=int(input(Back.GREEN+Fore.BLUE+" "*44+"Enter your Choise: "))
  if choise==1:
      add_student()
  elif choise==2:
      delete_student()
  elif choise==3:
      import search
      search.search_menu()
  elif choise==4:
      list_student()
student_menu()
  

 
