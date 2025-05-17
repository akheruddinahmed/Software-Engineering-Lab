class Student:
    def __init__(self, roll_no, name, branch, semester, percentage):
        self.roll_no = roll_no
        self.name = name
        self.branch = branch
        self.semester = semester
        self.percentage = percentage


student1 = Student(101, "John Doe", "Computer Science", 3, 85.5)
student2 = Student(102, "Jane Smith", "Electrical Engineering", 2, 78.3)


print("Student 1 Information:")
print("Roll No:", student1.roll_no)
print("Name:", student1.name)
print("Branch:", student1.branch)
print("Semester:", student1.semester)
print("Percentage:", student1.percentage)

print("\nStudent 2 Information:")
print("Roll No:", student2.roll_no)
print("Name:", student2.name)
print("Branch:", student2.branch)
print("Semester:", student2.semester)
print("Percentage:", student2.percentage)
