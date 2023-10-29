import sys
class Student:
    def __init__(self,student_name,student_id,student_class,enrolled_course,birth_year,address,parent_details):
        self.student_name = student_name
        self.student_id = student_id
        self.student_class=student_class
        self.enrolled_course=enrolled_course
        self.birth_year = birth_year
        self.address = address
        self.parent_details = parent_details

    def __str__(self):
        Info=self.student_name + ","
        Info+=self.student_id + ","
        Info+=self.student_class + ","
        Info+=self.enrolled_course + ","
        Info+=self.birth_year + ","
        Info+=self.address + ","
        Info+=self.parent_details + ""
        return Info

class StudentManager:
    def read_stripped_str(self, prompt):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        entered_stripped_str = sys.stdin.readline().strip()
        return entered_stripped_str

    def read_stripped_non_empty_str(self, prompt):
        entered_stripped_non_empty_str = self.read_stripped_str(prompt)
        while (len(entered_stripped_non_empty_str) == 0):
            entered_stripped_non_empty_str = self.read_stripped_str("Input cannot be empty! " + prompt)
        return entered_stripped_non_empty_str

    def read_int(self, prompt):
        entered_int = int(self.read_stripped_non_empty_str(prompt))
        return entered_int

    def __init__(self):
        students = []
        self.students = students

        menu_choice=""
        while(menu_choice!="X"):
            menu="--------------------------------\n"
            menu+="Student Manager menu\n"
            menu+="====================\n"
            menu+="[A]dd Students\n"
            menu+="[S]earch\n"
            menu+="[L]oad a file" '\n'
            menu+="E[x]it\n"
            menu+="\n"
            menu+="Enter your choice: "

            menu_choice = self.read_stripped_str(menu).upper()

            if (menu_choice=="A"):
                sys.stdout.write("-------------------------------\n")
                sys.stdout.write("Add Student - Student Manager\n")
                sys.stdout.write("================================\n")

                max_num_students = self.read_int("How many students would you like to add: ")

                a=0
                while(a<max_num_students):
                    sys.stdout.write("\n"+ "Entering student " + str(a+1) + " details...\n")

                    student_name = self.read_stripped_non_empty_str("Name: ")

                    student_id = self.read_stripped_non_empty_str("ID: ").upper()
                    while(student_id[0] != "M"):
                        student_id = self.read_stripped_non_empty_str("Invalid! Id must start with M: ").upper()

                    student_class = self.read_stripped_str("Enter class: ")

                    student_enrolled_course = self.read_stripped_non_empty_str("Enter Enrolled Course: ")


                    current_year=2021
                    student_birth_year = self.read_stripped_non_empty_str("Birth Year:")
                    while(int(student_birth_year)>= current_year):
                        student_birth_year = self.read_stripped_non_empty_str("Birth year cannot be in the future:  ")
                        student_birth_year = int(student_birth_year)

                    student_address = self.read_stripped_str("Address: ")

                    student_parent_details = self.read_stripped_str("Parent's Contact Detail: ")

                    new_student = Student(student_name,student_id,student_class,student_enrolled_course,student_birth_year,student_address,student_parent_details)
                    students.append(new_student)
                    a=a+1

                user_choose_to_save = self.read_stripped_str("Do you want to [S]ave these details[or press any other key to go back to main menu]: ").upper()
                if(user_choose_to_save=="S"):
                    File_Name = self.read_stripped_str("Enter name of the file in which you want to save these details: ")
                    Write_File = open(File_Name+".csv", "w")
                    i=0
                    while (i < len(students)):
                        Write_File.write(str(students[i]) + "\n")
                        i+=1
                    Write_File.close()
                    sys.stdout.write("Details Saved Successfully...\n")


            if(menu_choice=="S"):
                sys.stdout.write("--------------------------------\n")
                sys.stdout.write("Search Student - Student Manager\n")
                sys.stdout.write("================================\n")

                partial_name = self.read_stripped_str("Enter partial name to search: ")
                partial_name_uppercase = partial_name.upper()

                sys.stdout.write("S.no.\t")
                sys.stdout.write("Name" + "\t")
                sys.stdout.write("Id" + "\t")
                sys.stdout.write("Class" + "\t")
                sys.stdout.write("Course" + "\t")
                sys.stdout.write("Birth Year" + "\n")

                num_search_results=0
                i=0
                while(i<(len(students))):
                    if(partial_name_uppercase in students[i].student_name.upper() ):
                        student_name=students[i].student_name
                        student_id=students[i].student_id
                        student_class=students[i].student_class
                        student_enrolled_course=students[i].enrolled_course
                        student_birth_year=students[i].birth_year
                        student_address=students[i].address
                        student_parent_details=students[i].parent_details

                        sys.stdout.write(str(i+1) + "\t")
                        sys.stdout.write(students[i].student_name + "\t")
                        sys.stdout.write(students[i].student_id + "\t")
                        sys.stdout.write(students[i].student_class + "\t")
                        sys.stdout.write(students[i].enrolled_course+ "\t")
                        sys.stdout.write(str(students[i].birth_year) + "\n")
                        num_search_results=+1
                    i+=1

                if(num_search_results==0):
                    sys.stdout.write("No matches for: "+partial_name+"\n")

                else:
                    sub_menu_choice_record_number = self.read_int("Select record number: ")-1

                    sub_menu_operation ="[E]dit\n"
                    sub_menu_operation+="[R]emove\n"
                    sub_menu_operation+="or [x] to go back to main menu: "
                    sub_menu_choice_operation = self.read_stripped_non_empty_str(sub_menu_operation).upper()

                    if(sub_menu_choice_operation=="E"):
                        sys.stdout.write("Entering student "+str(sub_menu_choice_record_number+1)+" details...\n")

                        student_name = self.read_stripped_non_empty_str("Name: ")

                        student_id = self.read_stripped_non_empty_str("ID: ").upper()
                        while (student_id[0] != "M"):
                            student_id = self.read_stripped_non_empty_str("Invalid! Id must start with M: ").upper()

                        student_class=self.read_stripped_non_empty_str("Enter Class: ")

                        student_enrolled_course=self.read_stripped_non_empty_str("Enter Enrolled Course: ")

                        current_year = 2021
                        student_birth_year = self.read_stripped_non_empty_str("Birth Year:")
                        while (int(student_birth_year) >= current_year):
                            student_birth_year = self.read_stripped_non_empty_str("Birth year cannot be in the future:  ")
                            student_birth_year = int(student_birth_year)

                        student_address = self.read_stripped_str("Address: ")

                        student_parent_details = self.read_stripped_str("Parent's Contact Detail: ")

                        students[sub_menu_choice_record_number].student_name=student_name
                        students[sub_menu_choice_record_number].student_id=student_id
                        students[sub_menu_choice_record_number].student_class=student_class
                        students[sub_menu_choice_record_number].enrolled_course=student_enrolled_course
                        students[sub_menu_choice_record_number].birth_year=student_birth_year
                        students[sub_menu_choice_record_number].address=student_address
                        students[sub_menu_choice_record_number].parent_details=student_parent_details

                        File_Name=self.read_stripped_str("Enter name of the file: ")
                        Write_File = open(File_Name+".csv", "w")
                        i = 0
                        while (i < len(students)):
                            Write_File.write(str(students[i]) + "\n")
                            i += 1
                        Write_File.close()
                        sys.stdout.write("Details Updated Successfully...\n")


                    elif(sub_menu_choice_operation=="R"):
                        del(students[sub_menu_choice_record_number])
                        File_Name=self.read_stripped_str("Enter name of the file: ")
                        Write_File = open(File_Name+".csv", "w")
                        i = 0
                        while (i < len(students)):
                            Write_File.write(str(students[i]) + "\n")
                            i += 1
                        Write_File.close()
                        sys.stdout.write("Details Updated Successfully...\n")

                    else:
                        sys.stdout.write("Going Back To Main Menu...\n")

            if(menu_choice=="L"):
                name_of_the_file = self.read_stripped_str("Enter name of the file: ")
                load_file = open(name_of_the_file+".csv", "r")

                User_Entry = load_file.readline()
                while (len(User_Entry) > 0):
                    Details_Sections = User_Entry.split(",")
                    name = Details_Sections[0]
                    id = Details_Sections[1]
                    st_class = Details_Sections[2]
                    course = Details_Sections[3]
                    birth = Details_Sections[4]
                    address = Details_Sections[5]
                    details = Details_Sections[6]


                    sys.stdout.write("\n")
                    sys.stdout.write("Student Name: " + name + "\n")
                    sys.stdout.write("Student Id: " + id + "\n")
                    sys.stdout.write("Student Class: " + st_class + "\n")
                    sys.stdout.write("Enrolled Course: " + course + "\n" )
                    sys.stdout.write("Student Birth Year: " + birth + "\n")
                    sys.stdout.write("Student Address: " + address + "\n")
                    sys.stdout.write("Student Parent Details: " + details + "\n")
                    sys.stdout.write("\n")

                    User_Entry = load_file.readline()

                load_file.close()
                sys.stdout.write("Data Loaded Successfully...\n")

StudentManager()