import Student as st
import Courses as co
import Exam as ex
import Batch as bt
import Department as dep

print("CHOOSE ONE OF THE FOLLOWING MODULES WHICH YOU INTEND TO VISIT-"+"\n"+"1.Student"+"\n"+"2.Courses"+"\n"+"3.Batch"+"\n"+"4.Department"+"\n"+"5.Exam")
c=int(input("Enter choice number"))

if c==1:
    c2 = int(input("Choose one of the following functions " + "\n" + "1.Create Student" + "\n" + "2.Update student" +"\n"+"3.Remove student" + "\n" + "4.Generate Report card"))

    if c2 == 1:
        st.create_student()
    elif c2 == 2:
        st.update_student()
    elif c2 == 3:
        st.remove_student()
    elif c2 == 4:
        st.Report_Card()






elif c==2:
    c2 = int(input(
        "Choose one of the following functions " + "\n" + "1.Create course" + "\n" + "2.View course performance" + "\n"+"3.View course statistics"))

    if c2 == 1:
        co.create_course()

    elif c2 == 2:
        co.view_performance()

    elif c2 == 3:
        co.course_statistics()

elif c==3:
    c2 = int(input("Choose one of the following functions " + "\n" + "1.Create Batch" + "\n" + "2.View student list"+"\n"+ "3.View course list"+"\n"+"4.View complete batch performance"))
    if c2==1:
        bt.create_Batch()
    elif c2==2:
        bt.view_student()
    elif c2==3:
        bt.view_course()
    elif c2==4:
        bt.view_stud_performance()


elif c==4:
    c2 = int(input("Choose one of the following functions " + "\n" + "1.Create Department" + "\n" + "2.View batches in department" + "3.View average performance of batches"+"\n"+"4.View department statistics"))
    if c2==1:
        dep.Create_Department()
    elif c2==2:
        dep.View_Batches()
    elif c2==3:
        dep.View_Batch_Performance()
    elif c2==4:
        dep.department_statistics()


elif c==5:
    c2=int(input("Choose one of the following functions "+"\n"+"1.Create Exam"+"\n"+"2.View students performance in exam"+"3.View exam statistics"))
    if c2==1:
        ex.create_Exam()
    elif c2==2:
        ex.view_performance()
    elif c2==3:
        ex.exam_statistics()

