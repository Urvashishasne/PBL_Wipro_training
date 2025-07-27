def get_student_averages():
    n=int(input("enter the number of students: "))
    students={}
    for _ in range(n):
        name=input("enter student name")
        marks=input(f"enter marks for {name}")
        marks=list(map(float,marks.strip().split()))
        students[name] = marks
    query_name = input("enter the name to find average marks")
    if query_name in students:
        average= sum(students[query_name])/3
        print(f"average percentage mark for {query_name} : {average:.2f}")
    else:
        print("Student not Found.")

        
        