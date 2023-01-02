import pandas as pd
from matplotlib import pyplot
import numpy as np
def create_course():
    id=input("Enter course ID")
    name=input("Enter course name")
    data = {'Course ID': [id], 'Course Name': [name], 'Marks obtained':[""]}
    df = pd.DataFrame(data)
    df.to_csv("Course.csv", mode='a', index=False, header=False)

    print("Course created.The list of students and their respective marks will get updated as and when the exam marks are entered ")

def view_performance():
    id=input("Enter course ID=")
    dfc=pd.read_csv("Course.csv")
    dfs=pd.read_csv("Student.csv")
    mlist=[]
    course_name=""
    name=""
    roll=0
    for i in range(len(dfc)):
        if dfc.iat[i,0]==id:
            mlist=dfc.iat[i,2].split("-")#list of marks

            course_name=str(dfc.iat[i,1])#course name

            break

    print("\n\n")
    for i in range(len(mlist)):
        stm=mlist[i]#student marks pair
        stm=stm.split(":")
        stid=stm[0]#taking student ID

        mrk=stm[1]#taking student marks

        for j in range(len(dfs)):
            if dfs.iat[j,0]==stid:
                name=dfs.iat[j,1]#taking student name
                roll=dfs.iat[j,2]#taking student roll number
                break
        print("Student ID=" + str(stid))
        print("Student name="+str(name))
        print("Student roll no=" +str(roll))
        print("Student marks="+str(mrk)+"\n\n")

def course_statistics():
    course_ID=input("Enter course ID")
    dfc=pd.read_csv("Course.csv")
    marks=[]
    for i in range(len(dfc)):
        if dfc.iat[i,0]==course_ID:
            name=dfc.iat[i,1]
            sm_list=dfc.iat[i,2].split("-")#taking list of students and the marks
            for i in range(len(sm_list)):
                sm=sm_list[i].split(":")#splitting each student marks pair
                marks.append(int(sm[1]))#appending marks
            break
    print("STATISTICS FOR COURSE="+name+"("+course_ID+")")
    bin_range=[0,40,50,60,70,80,90,100]
    ref=['F','E','D','C','B','A']
    Yl=range(0,len(marks)+1)
    pyplot.hist(marks,bin_range)
    pyplot.xticks([20,55,65,75,85,95],ref)
    pyplot.yticks(Yl)
    pyplot.xlabel("OBTAINED GRADES")
    pyplot.ylabel("STUDENT FREQUENCY")
    pyplot.show()












