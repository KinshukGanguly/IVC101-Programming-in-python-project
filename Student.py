import pandas as pd


def create_student(*args):
    if len(args)==0:
        id = input("Enter student ID-")
        name = input("Enter student name-")
        roll = input("Enter class roll number-")
        batch = input("Enter batch ID-")
    else:
        id=args[0]
        name=args[1]
        roll=args[2]
        batch=args[3]

    data = {'Student ID': [id], 'Name': [name], 'Class Roll Number': [roll],'Batch ID':[batch]}
    df = pd.DataFrame(data)
    df.to_csv("Student.csv", mode='a', index=False, header=False)
    df2=pd.read_csv("Batch.csv")
    flag=1
    for i in range(len(df2)):
        if (str(df2.iat[i, 0])) == batch:
            flag=0
            st=str(df2.iat[i, 4])#extracting the list of existing students
            if id in st:#already id exists
              break
            else:
                if st=="nan":#empty string
                    st=id
                else:
                    st=st+":"+id#adding new id to existing string
                    df2.iat[i, 4]=st#updating string
                break
    df2.to_csv("Batch.csv", index=False)

    if flag==1:
        print("The entered batch ID doesn't exist")
    print("Student record updated successfully")


def update_student():
    id=input("Enter the student id whose record you want to update")
    df=pd.read_csv("Student.csv")
    for i in range(len(df)):
        if (str(df.iat[i, 0])) == id:
            choice=int(input("Enter 1 for changing name,2 for changing roll no,3 for changing batch ID"))
            data=input("enter the new data to be updated")
            if choice==3:
                name = df.iat[i, 1]
                roll = df.iat[i, 2]
                remove_student(id)
                create_student(id,name,roll,data)
            else:
                df.iat[i, choice] = data



    df.to_csv("Student.csv",index=False)




def remove_student(*args):
    if len(args)==0:
        id = input("ENTER STUDENT ID")
    else:
        id=args[0]

    print(type(id))
    df=pd.read_csv("Student.csv")
    for i in range(len(df)):
       if (str(df.iat[i,0]))==id:
           batch=df.iat[i,3]
           print("RECORD DELETED")
           df = df.drop(i)
           break
    df2 = pd.read_csv("Batch.csv")
    flag = 1
    for i in range(len(df2)):
        if (str(df2.iat[i, 0])) == batch:
            flag = 0
            st = str(df2.iat[i, 4])
            # extracting the list of existing students
            st=st.split(":")
            if id in st:  # already id exists
                st.remove(id)
                string=st[0]
                for i in range(1,len(st)):
                    string=string+":"+st[i]

                df2.iat[i, 4]=string


    df2.to_csv("Batch.csv", index=False)
    if flag == 1:
        print("The entered batch ID doesn't exist")
    df.to_csv("Student.csv",index=False)

def Report_Card():
    id=input("Enter Stuident ID")
    dfs=pd.read_csv("Student.csv")
    dfb=pd.read_csv("Batch.csv")
    dfc=pd.read_csv("Courses.csv")
    dfe=pd.read_csv("Examination.csv")
    marks=[]
    course_ID=[]
    course=[]
    name=""
    roll=0
    total=0
    batch_ID=""
    for i in range(len(dfs)):
        if dfs.iat[i,0]==id:
            name=dfs.iat[i,1]
            roll=dfs.iat[i,2]
            batch_ID=dfs.iat[i,3]
            break

    for i in range(len(dfb)):
        if dfb.iat[i,0]==batch_ID:
            st=dfb.iat[i,3]
            course_ID=st.split(":")#list of course IDs for that batch
            break
    for i in range(len(course_ID)):
        courseID=course_ID[i]#taking all courses one by one that are in batch
        for j in range(len(dfc)):
            if dfc.iat[j,0]==course_ID:#searching for the course
                course.append(dfc.iat[j,1])

                m = str((dfc.iat[j, 2])).split("-")#student-marks pair list for that course
                for k in range(len (m)):
                    sm=m[k].split(":")
                    if sm[0]==id:
                        marks.append(sm[1])


    f=open("Result.txt","w")
    f.write("NAME-"+name)
    f.write("STUDENT ID-"+id)
    f.write("BATCH ID-" + batch_ID)
    f.write("ROLL NUMBER-" + roll)
    f.write("COURSE\t\tCOURSE ID\t\tMARKS\t\tGRADE\t\tSTATUS" )
    for i in range(len(course)):
        total+=marks[i]
        list1=grade(marks[i])#list
        f.write(course[i]+"\t"+course_ID[i]+"\t"+marks[i]+'\t'+list1[0]+"\t"+list1[1])
    total=total/ len(course)
    f.write("OVER ALL GRADE="+grade(marks[i])[0])
    f.write("PASS STATUS=" + grade(marks[i])[1])
    f.close()
    print("The result shall be created in the same directory as the database")


def grade(marks):
    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    elif marks >= 50:
        grade = 'E'
    else:
        return 'F', 'Failed'
    return (grade, 'Passed')








