import csv

def write_into_csv(info_list):
    with open('Student_info.csv','a',newline='') as csv_file :
        writer = csv.writer(csv_file)


        if csv_file.tell()== 0:
            writer.writerow(["Name" , "Age" ," Contact Number" , "EmailId"])

        writer.writerow(info_list)
         
if_name_=='_main_':
 condition = True
 student_num=1

 while(condition):
    student_info = ("Enter student information for student  : ")

    student_info_list = student_info.split('')



    print("the entered statment is "
          .format(student_info_list[0],student_info_list[1],student_info_list[3])) 
    
    choice_check = input("is the entered info correct : ")

    if choice_check == "Yes" :
        write_into_csv(student_info_list)

        condition_check = input ("Enter yes\no if u want to enter the information for another student: ")
        if choice_check == "Yes" :
           condition = True
           student_numm = student_num +1 
        elif choice_check == "no" :
           print("please re enter the value !")

