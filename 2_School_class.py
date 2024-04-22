class School:
    def __init__(self, name, establishment_year):
        self.name = name
        self.establishment_year = establishment_year
        self.students = []
        self.teachers = {}

    def add_new_student(self, student_name, class_name):
        self.students.append((student_name, class_name))

    def add_new_teacher(self, teacher_name, subject):
        self.teachers[teacher_name] = subject

    def display_student_list(self):
        print("List of enrolled students in the school:")
        for student in self.students:
            print(f"{student[0]} - Class: {student[1]}")

    def display_teacher_list(self):
        print("List of teachers working in the school:")
        for teacher, subject in self.teachers.items():
            print(f"{teacher} - Subject: {subject}")

# Example usage:
school = School("Sample School", 1990)
school.add_new_student("Ali", "9A")
school.add_new_student("Ayşe", "10B")
school.add_new_teacher("Ahmet Hoca", "Mathematics")
school.add_new_teacher("Fatma Hoca", "History")

school.display_student_list()
school.display_teacher_list()