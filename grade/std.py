import grd
grademark = { }
while True:
    print("---all students grademarks---")
    print("1.add students:")
    print("2.view all students:")
    print("3.search student marks:") 
    print("4.update student marks:") 
    print("5.remove student:")  
    print("6.exit")
    choice = input("enter choice:")
    if choice == '1':
        grd.add_grade_marks(grademark)
    elif choice == '2':
        grd.view_all(grademark)
    elif choice == '3':
        grd.search_student(grademark)
    elif choice == '4':
        grd.update_student(grademark)
    elif choice == '5':
        grd.remove_student(grademark)
    elif choice == '6':
        print("existing----")
    else:
        print("invalid choice please try again")