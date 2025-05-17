class Student:
    def __init__(self, roll_no, subject1, subject2, subject3, subject4, subject5):
        self.roll_no = roll_no
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        self.subject4 = subject4
        self.subject5 = subject5

    def calculate_average_percentage(self):
        total_marks = self.subject1 + self.subject2 + self.subject3 + self.subject4 + self.subject5
        average_percentage = total_marks / 5
        return average_percentage



student1 = Student(101, 80, 85, 75, 90, 95)
student2 = Student(102, 70, 75, 85, 80, 90)


average_percentage_student1 = student1.calculate_average_percentage()
average_percentage_student2 = student2.calculate_average_percentage()


print("Average Percentage for Student 1 (Roll No:", student1.roll_no, "):", average_percentage_student1)
print("Average Percentage for Student 2 (Roll No:", student2.roll_no, "):", average_percentage_student2)
