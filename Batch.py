import pandas as pd
from matplotlib import pyplot
import numpy as np
def create_Batch():


    batch_ID=input("enter batch ID")
    batch_name=input("enter batch name")
    dept_ID=input("Enter department ID of the batch")
    n = int(input("Enter the number of courses taught in this batch"))
    courses = input("Enter course number 1")
    for i in range(n - 1):
        courses = courses + ":" + input("Enter course number " + str(i + 2))
    data = {'Batch ID': [batch_ID], 'Batch Name': [batch_name], 'Department ID': [dept_ID], 'List of Courses': [courses],
                'List of Students': [""]}
    df = pd.DataFrame(data)
    df.to_csv("Batch.csv", mode='a', index=False, header=False)
    dfd=pd.read_csv("Department.csv")
    for j in range(len(dfd)):
        if dfd.iat[j,0]==dept_ID:
            st=str(dfd.iat[j,2])
            if len(st)==0:
                st=batch_ID
            else:
                st=st+":"+batch_ID
            break





def view_course():
    dfb = pd.read_csv("Batch.csv")
    courses=[]
    batch_ID = input("enter batch ID")
    for i in range(len(dfb)):
        if dfb.iat[i,0]==batch_ID:
            courses=dfb.iat[i,3].split(":")
            break
    dfc=pd.read_csv("Course.csv")
    print ("The courses under this batch are-")
    course_ID=""
    for i in range(len(courses)):
        course_ID=courses[i]
        for j in range(len(dfc)):
            if dfc.iat[j,0]==course_ID:
                print("Course name="+str(dfc.iat[j,1])+"  Course ID="+course_ID)
                break

def view_student():
    dfb = pd.read_csv("Batch.csv")
    students = []
    batch_ID = input("enter batch ID")
    for i in range(len(dfb)):
        if dfb.iat[i, 0] == batch_ID:
            students = dfb.iat[i, 4].split(":")
            break
    dfs = pd.read_csv("Student.csv")
    print("The students in  batch are-")
    student_ID = ""
    for i in range(len(students)):
        student_ID = students[i]
        for j in range(len(dfs)):
            if dfs.iat[j, 0] == student_ID:
                print("Student name=" + dfs.iat[j, 1] + "  Student_Id="+student_ID+" Roll number="+dfs.iat[j, 2])
                break


def view_stud_performance():
    id=input("Enter batch ID")
    stud_list=[]
    curse_list=[]
    dfb=pd.read_csv("Batch.csv")
    dfc=pd.read_csv("Course.csv")
    for i in range(len(dfb)):
        if dfb.iat[i,0]:
            batch_name=dfb.iat[i,1]
            stud_list=dfb.iat[i,3].split(":")
            course_list=dfb.iat[i,2].split(":")
            break
    for i in range(len(stud_list)):
        st_ID=stud_list[i]
        name=''
        roll=0
        course_ID=""
        marks=[]
        dfs=pd.read_csv("Student.csv")
        for j in range(len(dfs)):
            if dfs.iat[j,0]==st_ID:
                name=dfs.iat[j,1]
                roll=dfs.iat[j,2]
                break
        print("Student name="+name+" Roll number="+roll+" ")
        #student details obtained
        for k in range(len(course_list)):
            course_ID=course_list[k]
            smlist=[]
            course_name=""
            dfc=pd.read_csv("Course.csv")
            m=0
            for l in range(len(dfc)):
                if dfc.iat[l,0]==course_ID:
                    smlist=str(dfc.iat[l,2]).split("-")
                    course_name=dfc.iat[l,1]
                    break
            #course details obtained

            for p in range(len(smlist)):
                sm=smlist[p]
                if st_ID in sm:
                    sm=sm.split(":")
                    m=int(sm[1])
                    marks.append(m)
                    break
            print("Marks in course "+course_name+"="+m)
        pyplot.pie(marks,label=course_list)



