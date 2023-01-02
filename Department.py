import pandas as pd
import  Exam as ex
from matplotlib import pyplot
import numpy as np
def Create_Department():
    name=input('Enter the department name')
    id=input("Enter department ID")

    data={'Department ID':[id],'Department Name':[name],'List of Batches':[""]}
    df = pd.DataFrame(data)
    df.to_csv("Department.csv",mode='a',index=False,header=False)
    print("The department has been created.The list of batches will be updated as and when the batches get created with this particular department id")

def View_Batches():
    id=input("Enter department ID")
    dfd=pd.read_csv("Department.csv")
    for i in range(len(dfd)):
        if dfd.iat[i,0]==id:
            str=dfd.iat[i,2]
            break
    batch_list=str.split(":")
    dfb=pd.read_csv("Batch.csv")
    print("LIST OF BATCHES UNDER THIS DEPARTMENT-")
    for i in range(len(batch_list)):
        batch_ID=batch_list[i]
        for j in range(len(dfb)):
            if dfb.iat[j,0]==batch_ID:
                print(batch_ID+"\t\t"+dfb.iat[j,2])
                break #for j


def View_Batch_Performance():
    dept_ID=input('Enter department ID')

    batch_studentList=[]
    dfb=pd.read_csv("Batch.csv")
    b_avg = []
    b_name = []
    course_avg=0
    batch_avg=0

    for i in range(len(dfb)):
        if dfb.iat[i,2]==dept_ID:
            batch_studentList.append([dfb.iat[i,0],dfb.iat[i,1],dfb.iat[i,3],dfb.iat[i,4]])

    for i in range(len(batch_studentList)):
        batch_detail=batch_studentList[i]
        batch_ID=batch_detail[0]
        batch_name=batch_detail[1]
        b_name.append(batch_name)
        print("BATCH NAME-"+batch_name)
        print("BATCH ID-" +batch_ID )

        course_list=batch_detail[2].split(":")
        #student_list=batch_detail[3].split(":")
        for j in range(len(course_list)):
            courseID=course_list[j]

            course_avg+=ex.average(batch_ID,courseID)

        batch_avg=course_avg/len(course_list)
        b_avg.append(batch_avg)
        course_avg=0
        print("BATCH AVERAGE="+str(batch_avg)+"\n")

def department_statistics():
    dept_ID = input('Enter department ID')

    batch_studentList = []
    dfb = pd.read_csv("Batch.csv")

    course_avg = 0

    b_name=[]
    b_avg=[]
    for i in range(len(dfb)):
        if dfb.iat[i, 2] == dept_ID:
            batch_studentList.append([dfb.iat[i,0],dfb.iat[i,1],dfb.iat[i,3]])

    for i in range(len(batch_studentList)):
        batch_detail = batch_studentList[i]
        batch_ID = batch_detail[0]

        b_name.append(batch_detail[1])#storing  batch names under this department


        course_list = batch_detail[2].split(":")
        # student_list=batch_detail[3].split(":")
        for j in range(len(course_list)):
            courseID = course_list[j]

            course_avg += ex.average(batch_ID, courseID)

        batch_avg = course_avg / len(course_list)
        b_avg.append(batch_avg)#storing the average marks of the batches
        course_avg = 0
    pyplot.plot(b_name,b_avg)
    pyplot.show()
















