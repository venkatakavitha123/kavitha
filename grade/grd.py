def add_grade_marks(grademark):
    name = input("enter name:")
    marks = input("enter marks:")
    mark_list = list(map(int, marks.split()))
    grademark[name] = mark_list
    print(f"{name}={mark_list}")  
def view_all(grademark):
    if not grademark:
        print("no students found")
        return
    print("----all student---")
    for name , marks in grademark.items():
        avg = sum(marks) / len(marks)
        print(f"{name}- marks : {marks} | avg : {avg : .2f}")
def search_student(grademark):
    search_name = input("enter student name to search:").lower()
    found = False
    for name , marks in grademark.items():
        if search_name is name.lower():
            avg = sum(marks) / len(marks)
            print(f"found : {name} - marks:{marks} | avg: {avg : .2f}")        
            found = True
        if not found:
            print("students not found")
def update_student(grademark):
    name = input("enter name to update:")
    if name in grademark:
        marks = input("enter new marks:")
        marks_list = list(map(int, input().split()))
        grademark[name] = marks_list
        print(f"{name} 's marks updated")
    else:
        print("student not found")
def remove_student(grademark):
    name = input("enter student name to remove:")
    if name in grademark:
        del grademark[name]
        print(f"{name} remove from grademark")
    else:
        print("student not found")
    