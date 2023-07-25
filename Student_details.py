
import csv

def write_into_csv(info_list):
    with open('Student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)


        if csv_file.tell() == 0:     #if the file is empty
            writer.writerow(["Name", "Age", "Contact_Num", "E-mail_ID"])


        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_count = 0
    while(condition):
        student_info = input("Enter student information for #{} in the following format (Name, Age, Contact_Number, E-mail_ID) : " .format(student_count))
        print("Entered student information : " + student_info)

        student_info_list = student_info.split(' ')
        print("Entered splitted info : "  + str(student_info_list))

        print("\nThe entered information is :\nName : {}\nAge : {}\nContact_Number : {}\nE-mail_ID : {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        check_info = input("Is the entered information is correct?(yes/no) :   ")
        if check_info == 'yes':
            write_into_csv(student_info_list)

            condition_check = input("Enter (yes/no) if you need to enter some more student information : ")
            if condition_check == 'yes':
                condition = True
                student_count = student_count + 1
            elif condition_check == 'no':
                condition = False
        elif check_info == 'no':
            print("\nRe-enter the information!")