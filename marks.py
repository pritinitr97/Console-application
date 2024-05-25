from os import *
import sys
from colorama import *
import pymysql

def marks_entry():
    system ('color 6f')
    system('cls')
    print('\n'*5)
    print(Back.YELLOW+Fore.BLUE+" "*44+" Marks Entry")
    print(Back.YELLOW+Fore.BLUE+" "*42+"--------------------")
    

            
    rno=int(input("Enter the roll no:"))
    s1=input("Enter the sub1:")
    s2=input("Enter the sub2:")
    s3=input("Enter the sub3:")
    s4=input("Enter the sub4:")
    s5=(input("Enter the sub5:"))
    m1=int(input("Enter the marks1:"))
    m2=int(input("Enter the marks2:"))
    m3=int(input("Enter the marks3:"))
    m4=int(input("Enter the marks4:"))
    m5=int(input("Enter the marks5:"))
    t=m1+m2+m3+m4+m5
    p=t*100/500
    if p>=80:
       g='A'
    elif p>=60:
         g='B'
    elif p>=40:
         g='C'
    else:
      g='D'
                    
                
    con=pymysql.connect(host='localhost',user='root',password='Abl@721101',db='college',autocommit=True)
    cur=con.cursor()
    q="insert into marks values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(rno,s1,s2,s3,s4,s5,m1,m2,m3,m4,m5,t,p,g)
    cur.execute(q,val)
    con.close()
    print("successfull saved .............................")
            
             
        
def delete_marks_entry():
    system ('color 4f')
    system('cls')
    print('\n'*5)
    print(Back.RED+Fore.YELLOW+" "*44+" Delete Marks Entry")
    print(Back.RED+Fore.YELLOW+" "*42+"---------------------------")
    n=int(input("Enter the roll no:"))
    con=pymysql.connect(host='localhost',user='root',password='Abl@721101',db='college',autocommit=True)
    cur=con.cursor()
    q="select * from marks where rno=%s"
    val=(n,)
    cur.execute(q,val)
    
    row=cur.fetchone()
    if row==None:
        print(Back.RED+Fore.YELLOW+" "*44+"Not found")
    else:
        print("Marks Record")
        print('-'*40)
        print(" Student's Rollno     :",row[0])
        print(row[1],   " : ",row[6])
        print(row[2],   " : ",row[7])
        print(row[3],   " : ",row[8])
        print(row[4],   " : ",row[9])
        print(row[5],   " : ",row[10])
        print(" Total marks      :",row[11])
        print("Percentage        :",row[12])
        print("Grade             :",row[13])
        
        ch=input("Delete it y/n ?")
        if ch in 'yY':
            q="delete from student where rno=%s"
            cur.execute(q,val)
            print("Successfully Deleted")


def list_marks_entry():
    system ('color 4f')
    system('cls')
    print('\n'*5)
    print(Back.RED+Fore.YELLOW+" "*60+" List Marks Entry")
    print(Back.RED+Fore.YELLOW+" "*50+"-----------------------------------------------")
    print(Back.RED+Fore.YELLOW+"%20s %20s %20s %20s "%("RNO","Total_Marks","Percetage","Grade"))
    print('-'*100)
    con=pymysql.connect(host='localhost',user='root',password='Abl@721101',db='college',autocommit=True)
    cur=con.cursor()
    q="select * from marks "
    cur.execute(q)
    for row in cur:
         print(Back.RED+Fore.YELLOW+"%20s %20s %20s %20s "%(row[0],row[11],row[12],row[13]))



def search_marks_entry():
    system ('color 4f')
    system('cls')
    print('\n'*5)
    print(Back.RED+Fore.YELLOW+" "*44+" Search Marks Entry")
    print(Back.RED+Fore.YELLOW+" "*42+"---------------------------")
    n=int(input("Enter the roll no:"))
    con=pymysql.connect(host='localhost',user='root',password='Abl@721101',db='college',autocommit=True)
    cur=con.cursor()
    q="select * from marks where rno=%s"
    val=(n,)
    cur.execute(q,val)
    
    row=cur.fetchone()
    if row==None:
        print(Back.RED+Fore.YELLOW+" "*44+"Not found")
    else:
        print("Marks Record")
        print('-'*40)
        print(" Student's Rollno     :",row[0])
        print("subject1 :",row[1],"Marks : ",row[6])
        print("subject2: ",row[2],"Marks : ",row[7])
        print("subject3: ",row[3],"Marks : ",row[8])
        print("subject4 :",row[4],"Marks : ",row[9])
        print("subject5 :",row[5],"Marks : ",row[10])
        print(" Total marks      :",row[11])
        print("Percentage        :",row[12])
        print("Grade             :",row[13])
        
        system('pause')


def edit_marks_entry():
    system ('color 4f')
    system('cls')
    print('\n'*5)
    print(Back.RED+Fore.YELLOW+" "*44+" Edit Marks Entry")
    print(Back.RED+Fore.YELLOW+" "*42+"---------------------------")
    n=int(input("Enter the roll no:"))
    con=pymysql.connect(host='localhost',user='root',password='Abl@721101',db='college',autocommit=True)
    cur=con.cursor()
    q="select * from marks where rno=%s"
    val=(n,)
    cur.execute(q,val)
    
    row=cur.fetchone()
    if row==None:
        print(Back.RED+Fore.YELLOW+" "*44+"Not found")
    else:
        print("Marks Record")
        print('-'*40)
        print(" Student's Rollno     :",row[0])
        print("subject1 :",row[1],"Marks : ",row[6])
        print("subject2: ",row[2],"Marks : ",row[7])
        print("subject3: ",row[3],"Marks : ",row[8])
        print("subject4 :",row[4],"Marks : ",row[9])
        print("subject5 :",row[5],"Marks : ",row[10])
        print(" Total marks      :",row[11])
        print("Percentage        :",row[12])
        print("Grade             :",row[13])
        
        
        ch=input("Edit it y/n ?")
        if ch in 'yY':
            s1=input('Enter subject1:')
            m1=input('Enter marks:')
            s2=input('Enter subject2:')
            m2=input('Enter marks:')
            s3=input('Enter subject3:')
            m3=input('Enter marks:')
            s4=input('Enter subject4:')
            m4=input('Enter marks:')
            s5=input('Enter subject5:')
            m5=input('Enter marks:')
            t=m1+m2+m3+m4+m5
            p=t*100/500
            if p>=80:
               g='A'
            elif p>=60:
                 g='B'
            elif p>=40:
                 g='C'
            else:
              g='D'
                    
            
            
            q="update marks set sub1=%s,sub2=%s,sub3=%s,sub4=%s,sub5=%s,marks1=%s,marks2=%s,marks3=%s,marks4=%s,marks5=%s,total=%s,per=%s,grade=%s where rno=%s"
            val=(s1,s2,s3,s4,s5,m1,m2,m3,m4,m5,t,p,g,n)
            cur.execute(q,val)
            print("sucessefully updated")
        
       

    
    
def marks_menu():
  system ('color 2f')
  system('cls')
  print('\n'*5)
  print(Back.GREEN+Fore.RED+" "*46+"MARKS MENU")
  print(Back.GREEN+Fore.RED+" "*42+"------------------")
  print(Back.GREEN+Fore.BLUE+" "*44+"1 marks entry")
  print(Back.GREEN+Fore.BLUE+" "*44+"2 delete marks entry")
  print(Back.GREEN+Fore.BLUE+" "*44+"3 edit marks entry")
  print(Back.GREEN+Fore.BLUE+" "*44+"4 search marks entry")
  print(Back.GREEN+Fore.BLUE+" "*44+"5 list of students")
  print(Back.GREEN+Fore.BLUE+" "*44+"3 back to main menu")
  print(Back.GREEN+Fore.RED+" "*42+"-----------------------")
  choise=int(input(Back.GREEN+Fore.BLUE+" "*44+"Enter your Choise: "))
  if choise==1:
      marks_entry()
      
  elif choise==2:
      delete_marks_entry()

  elif choise==3:
      edit_marks_entry()
  elif choise==4:
      search_marks_entry()
    
  elif choise==5:
      list_marks_entry()
      
  elif choise==6:
       return

marks_menu()
  

 
