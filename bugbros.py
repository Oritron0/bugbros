from datetime import date
from re import I
import mysql.connector
db = mysql.connector.connect(host="localhost", user="root", passwd="deepanshu", database="SGGSCC")
mycur = db.cursor()

student_id = ""
STUDENT_password = ""
STUDENT_NAME = ""
course = ""
semester = ""
roll_number = ""
TEACHER_PASS=""
TEACHER_SUB=""
TEACHER_NAM=""

def new_stu():  
    print("\nNEW STUDENT ID CREATION IN PROGRESS...")
    B = 1
    while B > 0:
        student_id = input("ENTER STUDENT ID:")
        if len(student_id) > 13:
            if str(student_id[len(student_id)-13:len(student_id)+1]) != "@sggscc.ac.in":
                print("STUDENT ID MUST BE OF FORM", "XYZ@sggscc.ac.in\n")
            else:
                A = 0
                sql = "SELECT STUDENT_ID FROM LOGIN"
                mycur.execute(sql)
                h = mycur.fetchall()
                for x in h:
                    if x[0] == student_id:
                        A = 1
                    else:
                        A += 0
                if A == 0:
                    B = 0
                    print("STUDENT ID ACCEPTED!!!\n")
                else:
                    print("STUDENT ID NOT AVAILABLE!!!\n")
        else:
            print("STUDENT ID MUST BE OF THE FORM ", "XYZ@sggscc.ac.in\n")
    A = 1
    while A > 0:
        STUDENT_password = input("ENTER password:")
        if len(STUDENT_password) < 8:
            print("password MUST BE ATLEAST 8 CHARACTERS!!!\n")
        else:
            A = 0
            print("password ACCEPTED!!!!\n")
    A = 1
    while A > 0:
        STUDENT_NAME = input("ENTER NAME:")
        if STUDENT_NAME == "":
            print("THIS FIELD CAN'T BE EMPTY!!!\n")
        else:
            print("NAME IS ACCEPTED!!!\n")
            A = 0
    A = 1
    while A > 0:
        course = (input("ENTER COURSE:"))
        A = 0

    A = 1
    while A > 0:
        semester = int(input("\nENTER SEMESTER:"))
        if semester > 6:
            print("SEMESTER NOT VALID.")
        A = 0

    A = 1
    while A > 0:
        roll_number = input("\nENTER ROLL NUMBER:")
        if roll_number == "":
            print("THIS FIELD CAN'T BE EMPTY!!!\n")
        else:
            A = 0
            pass
    sql = "INSERT INTO LOGIN values(%s,%s,%s,%s,%s,%s)"
    val = (student_id, roll_number, STUDENT_NAME,STUDENT_password, course, semester)

    student_id=student_id[:-13]
    sql_2="ALTER TABLE CPP ADD "+student_id+" varchar(2)"
    sql_3="ALTER TABLE CSA ADD "+student_id+" varchar(2)"
    sql_4="ALTER TABLE MATHS ADD "+student_id+" varchar(2)"
    sql_5="ALTER TABLE AECC ADD "+student_id+" varchar(2)"
    mycur.execute(sql, val)
    mycur.execute(sql_2)
    mycur.execute(sql_3)
    mycur.execute(sql_4)
    mycur.execute(sql_5)
    db.commit()
    print("YOUR ACCOUNT REGISTERATION IS COMPLETE!!!!!!\n")

def new_tea():
    # id, name , sub1, sub2 , pass
    print("\nNEW TEACHER ID CREATION IN PROGRESS...")
    B = 1
    while B > 0:
        teacher_id = input("ENTER TEACHER ID:")
        if len(teacher_id) > 7:
            if str(teacher_id[len(teacher_id)-7:len(teacher_id)+1]) != "@sggscc":
                print("TEACHER ID MUST BE OF FORM", "XYZ@sggscc\n")
            else:
                A = 0
                sql = "SELECT TEACHER_ID FROM TEACHERS"
                mycur.execute(sql)
                h = mycur.fetchall()
                for x in h:
                    if x[0] == teacher_id:
                        A = 1
                    else:
                        A += 0
                if A == 0:
                    B = 0
                    print("TEACHER ID ACCEPTED!!!\n")
                else:
                    print("TEACHER ID NOT AVAILABLE!!!\n")
        else:
            print("TEACHER ID MUST BE OF THE FORM ", "XYZ@sggscc\n")
    A = 1
    while A > 0:
        teacher_password = input("ENTER password:")
        if len(teacher_password) < 8:
            print("password MUST BE ATLEAST 8 CHARACTERS!!!\n")
        else:
            A = 0
            print("password ACCEPTED!!!!\n")
    A = 1
    while A > 0:
        TEACHER_NAME = input("ENTER NAME:")
        if TEACHER_NAME == "":
            print("THIS FIELD CAN'T BE EMPTY!!!\n")
        else:
            print("NAME IS ACCEPTED!!!\n")
            A = 0
    A = 1
    while A > 0:
        TEACHER_SUBJ = (input("ENTER SUBJECT 1:"))
        A = 0

    A = 1
    while A > 0:
        TEACHER_SUBJ2 = input("ENTER SUBJECT 2(Enter nil if none):")
        A = 0
    sql = "INSERT INTO TEACHERS values(%s,%s,%s,%s,%s)"
    val = (teacher_id,TEACHER_NAME,TEACHER_SUBJ,TEACHER_SUBJ2,teacher_password)
    # id, name , sub1, sub2 , pass 
    teacher_id=teacher_id[:-13]
    mycur.execute(sql, val)
    db.commit()
    print("YOUR ACCOUNT REGISTERATION IS COMPLETE!!!")

def delete_stud():
    print("DELETION IN PROGRESS...")
    C = 1
    while C>0:
        A=0
        student_id=input("\nENTER STUDENT ID:")
        sql="SELECT STUDENT_ID FROM LOGIN"
        mycur.execute(sql)
        h=mycur.fetchall()
        for x in h:
            if x[0]==student_id:
                    A=1
            else:
                    pass
            if A==1:
                B=1
                while B>0:#password check for fetch data block
                        Password=input("ENTER PASSWORD:")
                        sql="SELECT STUDENT_PASSWORD,STUDENT_ID FROM LOGIN WHERE STUDENT_ID=student_id"
                        mycur.execute(sql)
                        h=mycur.fetchall()
                        for x in h:
                            if x[1]==student_id:
                                if x[0]==Password:
                                    B=1
                                    while B>0:
                                        q=(input("ARE YOU SURE TO DELETE THIS STUDENT ID(YES OR NO)??")).upper()[0]
                                        if q=="Y":
                                            sql="DELETE FROM LOGIN WHERE STUDENT_ID=%s"
                                            mycur.execute(sql,(student_id,))
                                            db.commit()
                                            print("\nYOUR ACCOUNT IS NOW DELETED...")
                                            B=0
                                            C=0
                                        elif q=="N":
                                            print("OK!! THE ACOUNT IS NOT DELETED\n")
                                            B=0
                                            C=0
                                        else:
                                            print("NO SUCH OPTION EXISTS!!!\n")
                            else:
                                pass
                        if B!=0:
                            print("INCORRECT PASSWORD!!!\n")
            else:
                    print("\nNO SUCH STUDENT ID FOUND IN THE SYSTEM!!!\n")
                    
def delete_teacher():
    print("DELETION IN PROGRESS...")
    C = 1
    while C>0:
        A=0
        teacher_id=input("\nENTER TEACHER ID:")
        sql="SELECT TEACHER_ID FROM TEACHERS"
        mycur.execute(sql)
        h=mycur.fetchall()
        for x in h:
            if x[0]==teacher_id:
                    A=1
            else:
                    pass
        if A==1:
            B=1
            while B>0:#password check for fetch data block
                password=input("ENTER PASSWORD:")
                sql="SELECT TEACHER_PASS,TEACHER_ID FROM TEACHERS WHERE TEACHER_ID=teacher_id"
                mycur.execute(sql)
                h=mycur.fetchall()
                for x in h:
                    if x[1]==teacher_id:
                        if x[0]==password:
                            B=1
                            while B>0:
                                q=(input("ARE YOU SURE TO DELETE THIS STUDENT ID(YES OR NO)??")).upper()[0]
                                if q=="Y":
                                    sql="DELETE FROM TEACHERS WHERE TEACHER_ID=%s"
                                    mycur.execute(sql,(teacher_id,))
                                    db.commit()
                                    print("\nYOUR ACCOUNT IS NOW DELETED...")
                                    B=0
                                    C=0
                                elif q=="N":
                                    print("OK!! THE ACOUNT IS NOT DELETED\n")
                                    B=0
                                    C=0
                                else:
                                    print("NO SUCH OPTION EXISTS!!!\n")
                    else:
                        pass
                if B!=0:
                    print("INCORRECT PASSWORD!!!\n")
        else:
            print("\nNO SUCH TEACHER ID FOUND IN THE SYSTEM!!!\n")

def fee_find():
    id_fee=input("Enter student id:")
    sql = "SELECT STUDENT_ID FROM LOGIN"
    mycur.execute(sql)
    h = mycur.fetchall()
    for x in h:
        if x[0] == id_fee:
            A = 1
        else:
           pass
    if A == 1:
        sql = "SELECT * FROM fee"
        mycur.execute(sql)
        h = mycur.fetchall()
        print("| STUDENT_ID\t\t       | FEE\t |")
        for i in h:
            print("|",i[0]," "*(22-len(i[0])),"|",i[1]," "*(6-len(i[1])),"|")
        
    else:
        print("NO SUCH STUDENT ID EXIST!!")

def fee_updt():
    id_fee=input("Enter student id:")
    sql = "SELECT STUDENT_ID FROM LOGIN"
    mycur.execute(sql)
    h = mycur.fetchall()
    for x in h:
        if x[0] == id_fee:
            A = 1
        else:
            pass
    if A == 1:
        fee=input("PAID OR DUE:")
        sql = "INSERT INTO FEE VALUES(%s,%s)"
        mycur.execute(sql,(id_fee,fee))
        db.commit()
        print("FEE STATUS UPDATED!!")
        
    else:
        print("NO SUCH STUDENT ID EXIST!!")



def admin():
    cou=1
    while cou>0:
        print("\n1.)NEW STUDENT")
        print("2.)NEW TEACHER")
        print("3.)DELETE STUDENT")
        print("4.)DELETE TEACHER")
        print("5.)DISPLAYING FEE RECORD")
        print("6.)CREATING FEE RECORD")
        choice_1 = int(input("SELECT OPTION:"))
        if choice_1 == 1:
            new_stu()

        if choice_1 == 2:
            new_tea()
        
        if choice_1== 3:
            delete_stud()
        
        if choice_1== 4:
            delete_teacher()
            
        if choice_1== 5:
            fee_find()
            
        if choice_1==6:
            fee_updt()
            
        if choice_1==7:
            cou=0
            print("EXITTING..\n\n")
 
 
           
def pass_change():
    print("LOGGING IN...\n")
    C = 1
    while C > 0:
        A = 0
        student_id = input("ENTER STUDENT ID:")
        sql = "SELECT STUDENT_ID FROM LOGIN"
        mycur.execute(sql)
        h = mycur.fetchall()
        print(h)
        for x in h:
            if x[0] == student_id:
                A = 1
            else:
                pass
        if A == 1:
            print(student_id)

    A = 1  # pass_change block for updating info after fetching data
    while A > 0:
        im = input("\nENTER NEW password:")
        sql = "UPDATE LOGIN SET STUDENT_password=%s WHERE STUDENT_ID=%s"
        val = (im, student_id)
        mycur.execute(sql, val)
        db.commit()
        print("password UPDATED!!!\n")
        A = 0

def fetchdata():  # block for fetching data
    print("LOGGING IN...\n")
    C = 1
    while C > 0:
        A = 0
        student_id = input("ENTER STUDENT ID:")
        sql = "SELECT STUDENT_ID FROM LOGIN"
        mycur.execute(sql)
        h = mycur.fetchall()
        for x in h:
            if x[0] == student_id:
                A = 1
            else:
                pass
        if A == 1:
            B = 1
            while B > 0:  # password check for fetch data block
                STUDENT_password = input("ENTER password:")
                sql = "SELECT STUDENT_ID,STUDENT_PASSWORD FROM LOGIN WHERE STUDENT_ID=student_id"
                mycur.execute(sql)
                h = mycur.fetchall()
                for x in h:
                    if x[0] == student_id:
                        if x[1] == STUDENT_password:
                            B = 0
                            print("\nLOGIN SUCCESSSFUL\n")
                            sql = "SELECT * FROM LOGIN WHERE STUDENT_ID=student_id"
                            mycur.execute(sql)
                            h = mycur.fetchall()
                            for x in h:
                                if x[0] == student_id:
                                    print("YOUR ACCOUNT DETAILS:")
                                    print("ROLL NUMBER:", x[1])
                                    print("STUDENT NAME:", x[3])
                                    print("COURSE:", x[4],"\n")
                                    C = 0
                                else:
                                    pass
                        else:
                            pass
                if B != 0:
                    print("INCORRECT password!!!")
        else:
            print("NO SUCH STUDENT ID EXIST!!")
 
def attendence(ID):
    sub=["CSA","MATHS","AECC"]
    sql = "SELECT DATE , "+ID[:-13]+" FROM CPP"
    mycur.execute(sql)
    h = mycur.fetchall()
    print(h)
 
 
def student():
    cou=1
    fetchdata()
    while cou>0: 
        print("OPTIONS:")
        print("1.)Check classroom")
        print("2.)Check announcements")
        print("3.)Check assignments")
        print("4.)Check time table")
        print("5.)Check attendence")
        print("6.)Check fee status")
        print("7.)Display student review")
        print("8.)Change password")
        print("9.)Exit")
        choice_2 = int(input("SELECT OPTION:"))
        if choice_2 == 1:
            sql = "SELECT * FROM CLASSROOM"
            mycur.execute(sql)
            h = mycur.fetchall()
            print("\n|","ROOM NUMBER | ","SUBJECT")
            for i in h:
                print("|",i[0],"         | ",i[1])
            print('\n')
            
        if choice_2 == 2:
            sql = "SELECT * FROM ANNOUNCEMENT"
            mycur.execute(sql)
            h = mycur.fetchall()
            print("\nANNOUNCEMENTS:")
            for i in h:
                print(i[0],"\n\t\t\t\t\t\t-",i[1],"(",i[2],")\n")
                
                
            
        if choice_2 == 3:
            sql = "SELECT * FROM ASSIGNMENT"
            mycur.execute(sql)
            h = mycur.fetchall()
            print("\nASSIGNMENTS:")
            for i in h:
                print(i[0],"\nBY-",i[1],"\nDUE DATE-",i[2],"\n")

        elif choice_2 == 4:
            sql = "SELECT * FROM TIME_TABLE"
            mycur.execute(sql)
            h = mycur.fetchall()
            for i in h:
                print("|",i[0]," "*(12-len(i[0])),i[1]," "*(14-len(i[1])),i[2]," "*(14-len(i[2])),i[3]," "*(14-len(i[3])),i[4]," "*(14-len(i[4])))
            print("\n")
            
            
        if choice_2 == 5:
            attendence(student_id)
            
        if choice_2 == 6:
            id_fee=input("Enter student id:")
            sql = "SELECT STUDENT_ID FROM LOGIN"
            mycur.execute(sql)
            h = mycur.fetchall()
            for x in h:
                if x[0] == id_fee:
                    A = 1
                else:
                    pass
            if A == 1:
                sql = "SELECT * FROM fee"
                mycur.execute(sql)
                h = mycur.fetchall()
                print("|STUDENT_ID\t\t\t|FEE\t|")
                for i in h:
                    print("|",i[0]," "*(22-len(i[0])),"|",i[1]," "*(7-len(i[1])))
                
            else:
                print("NO SUCH STUDENT ID EXIST!!")
                
        if choice_2 == 7:
            sql = "SELECT * FROM STU_REV"
            mycur.execute(sql)
            h = mycur.fetchall()
            print("Your review is:")
            for i in h:
                if i[0]==student_id:
                    print(i[1])
        
        if choice_2==8:
            pass_change()
        
        if choice_2==9:
            cou=0
            print("EXITTING..\n\n")
      
      
        
def teacher_login():
    global TEACHER_SUB
    global TEACHER_NAM
    print("LOGGING IN...\n")
    C = 1
    while C > 0:
        A = 0
        teacher_id = input("ENTER TEACHER ID:")
        sql = "SELECT TEACHER_ID FROM TEACHERS"
        mycur.execute(sql)
        h = mycur.fetchall()
        for x in h:
            if x[0] == teacher_id:
                A = 1
            else:
                pass
        if A == 1:
            B = 1
            while B > 0:  # password check for fetch data block
                teacher_pass = input("ENTER password:")
                sql = "SELECT TEACHER_ID,TEACHER_PASS,SUBJECT_1,TEACHER_NAME FROM TEACHERS WHERE TEACHER_ID=teacher_id"
                mycur.execute(sql)
                h = mycur.fetchall()
                for x in h:
                    if x[0] == teacher_id:
                        if x[1] == teacher_pass:
                            B = 0
                            C=0
                            print("\nLOGIN SUCCESSSFUL\n")
                            print("Wecome "+teacher_pass)
                            TEACHER_SUB=x[2]
                            TEACHER_NAM=x[3]
                        else:
                            pass
                if B != 0:
                    print("INCORRECT password!!!")
        else:
            print("NO SUCH TEACHER ID EXIST!!")

def teacher():
    cou=1
    teacher_login()
    while cou>0:
        print("\n1.)Add new announcement")
        print("2.)Add new assignments")
        print("3.)Mark attendence")
        print("4.)Check Schedule")
        print("5.)Give out student review")
        print("6.)Exit")
        choice_3=int(input("SELECT OPTION:"))
        if choice_3==1:
            anno=input("Enter the announcements:")
            DATE=input("Enter date(Format-->DD-MM-YYYY):")
            sql = "INSERT INTO ANNOUNCEMENT values(%s,%s,%s)"
            val = (anno,TEACHER_NAM,DATE)
            mycur.execute(sql,val)
            db.commit()
            print("ANNOUNCEMENT POSTED!!")
            
        if choice_3==2:
            assi=input("Enter the assignments:")
            Date_1=input("Enter due date(Format-->DD-MM-YYYY):")
            sql = "INSERT INTO assignment values(%s,%s,%s)"
            val = (assi,TEACHER_NAM,Date_1)
            mycur.execute(sql,val)
            db.commit()
            print("ASSIGNMENT POSTED!!")
        
        
        if choice_3==3:
            Date=input("Enter date(Format-->DD-MM-YYYY):")
            sql = "SELECT STUDENT_ID FROM login"
            mycur.execute(sql)
            h = mycur.fetchall()
            attendence=[]
            sta=(Date,)
            for i in h:
                a=i[0][:-19]+":"
                atten=input(a)
                if atten=="A" or "P":
                    attendence+=[atten]
                    sta+=(atten,)
                else:
                    print("Enter P or A for attendence.")
            N=(("%"+"s,")*(len(attendence)))+"%s)"
            sql = "INSERT INTO "+TEACHER_SUB+" VALUES("+N
            mycur.execute(sql,sta)
            db.commit()
            print("Attendence Marked.")

        if choice_3==4:
            name=""
            for i in TEACHER_NAM:
                if i==" ":
                    break
                name+=i
            sql = "SELECT * FROM "+name
            mycur.execute(sql)
            h = mycur.fetchall()
            print("\n")
            for i in h:
                print("|",i[0]," "*(12-len(i[0])),"|",i[1],"|"," "*(14-len(i[1])),i[2],"|"," "*(14-len(i[2])),i[3],"|"," "*(14-len(i[3])),i[4]," "*(14-len(i[4])),"|")
            print("\n")

        if choice_3==5:
            sql = "SELECT STUDENT_ID FROM login"
            mycur.execute(sql)
            h = mycur.fetchall()
            for i in h:
                a=i[0][:-19]+":"
                sturev=input(a)
                sql = "INSERT INTO STU_REV VALUES(%s,%s)"
                sta(a,sql)
                mycur.execute(sql,sta)
                db.commit()
                print("REVIEW POSTED!!\n")
        if choice_3==6:
            cou=0
            print("EXITTING...\n\n")



def menu():
    c = 'y'
    while c == 'y':
        print("1.)STUDENT")
        print("2.)TEACHER")
        print("3.)ADMIN")
        print("4.)EXIT")
        choice = int(input("SELECT PROFILE:"))
        if choice == 3:
            pas = input("Enter password:")
            if pas == "admin@123":
                admin()
        elif choice == 1:
            student()
        elif choice == 2:
            teacher()
        elif choice == 4:
            print("EXITTING...")
            c=0
        else:
            print("INVALID INPUT")



menu()
