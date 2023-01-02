import pandas as pd
from matplotlib import pyplot
import numpy as np
def create_Exam():
    course_ID=input("Enter course ID")
    student_ID=input("Enter student ID")
    marks=input("Enter marks")
    s=""
    dfc=pd.read_csv("Course.csv")
    print(dfc)
    for i in range(len(dfc)):
        if dfc.iat[i,0]==course_ID:
            s=str(dfc.iat[i,2])

            if s=="nan":
                s=student_ID+":"+marks
            else:
                s=s+"-"+student_ID+":"+marks
            dfc.iat[i,2]=s
    print(dfc)
    dfc.to_csv("Course.csv",index=False)

def view_performance():
    course_ID=input('Enter course ID')
    dfc=pd.read_csv("Course.csv")
    dfs=pd.read_csv("Student.csv")


    for i in range(len(dfc)):
        if dfc.iat[i,0]==course_ID:
            s=dfc.iat[i,2]
            course_name=dfc.iat[i,1]
            list1=s.split("-")
            break
    for i in range (len(list1)):
        list2=list[1].split(":")
        list1[i]=list2
    print("PERFORMANCE FOR COURSE-"+course_name+"("+course_ID+")")
    print("STUDENT NAME\t\tSTUDENT ID\t\tMARKS" )
    for i in range(len(list1)):
        sub=list1[i]#taking studentid marks pair list
        student_ID=sub[0]
        marks=sub[1]
        for j in range(len(dfs)):
            if dfs.iat[j,0]==student_ID:
                print(dfs.iat[j,1]+"\t\t"+student_ID+"\t\t"+marks)
                break#for j





def exam_statistics():
    dfb = pd.read_csv("Batch.csv")
    dfc = pd.read_csv("Course.csv")

    batch_name = []
    batch_marks = []
    for i in range(len(dfc)):
        course_id = str(dfc.iat[i, 0])
        print("Course ID" + course_id)
        batch_name = []
        batch_marks = []
        dfb = pd.read_csv("Batch.csv")
        for j in range(len(dfb)):
            course_list = str(dfb.iat[j, 3])
            batch_id = str(dfb.iat[j, 0])
            if course_id in course_list:
                batch_name.append(batch_id)
                batch_marks.append(average(batch_id, course_id))
        x = np.array(batch_marks)
        y = np.array(batch_name)
        pyplot.scatter(x, y)
    pyplot.show()


def average(batch_id, course_id):
    dfb = pd.read_csv("Batch.csv")
    dfc = pd.read_csv("Course.csv")

    for i in range(len(dfb)):
        if (dfb.iat[i, 0] == batch_id):
            student = str(dfb.iat[i, 4])
            break

    student_list = student.split(":")
    # dfm=pd.read_csv(marks. csv)
    for j in range(len(dfc)):
        if dfc.iat[j, 0] == course_id:
            marks = str(dfc.iat[j, 2]).split("-")
            break
    print(marks)
    avg = 0
    for j in range(len(student_list)):
        id = student_list[j]
        for i in range(len(marks)):

            sm = marks[i].split(":")

            if sm[0] == id:
                avg = avg + int(sm[1])
                break
    avg = avg / len(student_list)
    print(avg)
    return avg


