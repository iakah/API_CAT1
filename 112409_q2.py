class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}
    
    def add_assignment_grade(self, assignment_name, grade):
        """Add an assignment and its grade"""
        if 0 <= grade <= 100:
            self.assignments[assignment_name] = grade
            print(f"Grade {grade} added for {assignment_name}")
            return True
        else:
            print("Grade must be between 0 and 100")
            return False
    
    def display_grades(self):
        """Display all assignments and grades for this student"""
        if not self.assignments:
            print(f"{self.name} has no assignments yet")
        else:
            print(f"\n{self.name}'s Grades:")
            total_points = 0
            for assignment, grade in self.assignments.items():
                print(f"  {assignment}: {grade}/100")
                total_points += grade
            
            average = total_points / len(self.assignments)
            print(f"  Average: {average:.2f}/100")
    
    def get_average_grade(self):
        """Calculate and return the average grade"""
        if not self.assignments:
            return 0
        return sum(self.assignments.values()) / len(self.assignments)
    
    def __str__(self):
        return f"{self.name} (ID: {self.student_id})"


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []
    
    def add_student(self, student):
        """Add a student to the course"""
        if student not in self.students:
            self.students.append(student)
            print(f"{student.name} added to {self.course_name}")
            return True
        else:
            print(f"{student.name} is already enrolled in {self.course_name}")
            return False
    
    def assign_grade(self, student_id, assignment_name, grade):
        """Assign a grade to a student for a specific assignment"""
        student = self.find_student_by_id(student_id)
        if student:
            return student.add_assignment_grade(assignment_name, grade)
        else:
            print(f"Student with ID {student_id} not found")
            return False
    
    def find_student_by_id(self, student_id):
        """Find a student by their ID"""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def display_all_students_grades(self):
        """Display all students and their grades"""
        if not self.students:
            print(f"No students enrolled in {self.course_name}")
            return
        
        print(f"\n{self.course_name} - All Students and Grades")
        print("=" * 50)
        
        for student in self.students:
            print(f"\nStudent: {student}")
            if student.assignments:
                for assignment, grade in student.assignments.items():
                    print(f"  {assignment}: {grade}/100")
                average = student.get_average_grade()
                print(f"  Average: {average:.2f}/100")
            else:
                print("  No assignments yet")
    
    def display_students(self):
        """Display all enrolled students"""
        if not self.students:
            print(f"No students enrolled in {self.course_name}")
        else:
            print(f"\nStudents in {self.course_name}:")
            for i, student in enumerate(self.students, 1):
                print(f"{i}. {student}")
    
    def get_class_average(self):
        """Calculate the class average"""
        if not self.students:
            return 0
        
        total_average = 0
        students_with_grades = 0
        
        for student in self.students:
            if student.assignments:
                total_average += student.get_average_grade()
                students_with_grades += 1
        
        if students_with_grades == 0:
            return 0
        
        return total_average / students_with_grades
    
    def __str__(self):
        return f"Instructor: {self.name}, Course: {self.course_name}"


def main():
    print("Welcome to the Online Course Management System")
    
    # Create instructor
    instructor_name = input("Enter instructor name: ").strip()
    course_name = input("Enter course name: ").strip()
    instructor = Instructor(instructor_name, course_name)
    
    # Add some sample students
    sample_students = [
        Student("Grace Wanjiku", "CS001"),
        Student("David Kiprop", "CS002"),
        Student("Fatuma Said", "CS003"),
        Student("John Mwangi", "CS004")
    ]
    
    print(f"\nAdding sample students to {course_name}:")
    for student in sample_students:
        instructor.add_student(student)
    
    while True:
        print(f"\nCourse Management System - {course_name}")
        print("1. Add new student")
        print("2. Assign grade to student")
        print("3. Display all students")
        print("4. Display specific student's grades")
        print("5. Display all students and grades")
        print("6. Show class statistics")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            # Add new student
            name = input("Enter student name: ").strip()
            student_id = input("Enter student ID: ").strip()
            
            # Check if student ID already exists
            if instructor.find_student_by_id(student_id):
                print(f"Student with ID {student_id} already exists")
            else:
                new_student = Student(name, student_id)
                instructor.add_student(new_student)
        
        elif choice == '2':
            # Assign grade to student
            if not instructor.students:
                print("No students enrolled. Please add students first.")
                continue
            
            instructor.display_students()
            student_id = input("\nEnter student ID: ").strip()
            
            student = instructor.find_student_by_id(student_id)
            if student:
                assignment_name = input("Enter assignment name: ").strip()
                try:
                    grade = float(input("Enter grade (0-100): "))
                    instructor.assign_grade(student_id, assignment_name, grade)
                except ValueError:
                    print("Please enter a valid number for the grade")
            else:
                print(f"Student with ID {student_id} not found")
        
        elif choice == '3':
            # Display all students
            instructor.display_students()
        
        elif choice == '4':
            # Display specific student's grades
            if not instructor.students:
                print("No students enrolled.")
                continue
            
            instructor.display_students()
            student_id = input("\nEnter student ID: ").strip()
            
            student = instructor.find_student_by_id(student_id)
            if student:
                student.display_grades()
            else:
                print(f"Student with ID {student_id} not found")
        
        elif choice == '5':
            # Display all students and grades
            instructor.display_all_students_grades()
        
        elif choice == '6':
            # Show class statistics
            if not instructor.students:
                print("No students enrolled.")
                continue
            
            print(f"\nClass Statistics for {course_name}")
            print(f"Total students: {len(instructor.students)}")
            
            students_with_grades = sum(1 for student in instructor.students if student.assignments)
            print(f"Students with grades: {students_with_grades}")
            
            if students_with_grades > 0:
                class_avg = instructor.get_class_average()
                print(f"Class average: {class_avg:.2f}/100")
                
                # Find highest and lowest averages
                student_averages = []
                for student in instructor.students:
                    if student.assignments:
                        avg = student.get_average_grade()
                        student_averages.append((student.name, avg))
                
                if student_averages:
                    student_averages.sort(key=lambda x: x[1], reverse=True)
                    print(f"Highest average: {student_averages[0][0]} ({student_averages[0][1]:.2f})")
                    print(f"Lowest average: {student_averages[-1][0]} ({student_averages[-1][1]:.2f})")
        
        elif choice == '7':
            print(f"Thank you for using the Course Management System!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()