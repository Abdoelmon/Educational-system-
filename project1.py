class Person:
    def __init__(self, name, user_name, password):
        self.name = name
        self.user_name = user_name
        self.password = password

class Student(Person):
    def __init__(self, user_name, password, name, id, email):
        super().__init__(name, user_name, password)
        self.id = id
        self.email = email
        self.registered_courses = []
        self.assignment_solutions = []

    def register_course(self, course):
        self.registered_courses.append(course)
        course.students.append(self)

    def list_courses(self):
        return self.registered_courses

    def view_course(self, course_code):
        for course in self.registered_courses:
            if course.code == course_code:
                return course
        return None

    def submit_assignment(self, course_code, assignment_title, solution):
        course = None  
        for c in self.registered_courses:
            if c.code == course_code:
                course = c
                break 

        if course:
            assignment = None
            for a in course.assignments:
                if a.title == assignment_title:
                    assignment = a
                    break
            
            if assignment:
                submission = AssignmentSolution(self, assignment, solution)
                assignment.submissions.append(submission)
                return submission
        return None

class Doctor(Person):
    def __init__(self, user_name, password, name):
        super().__init__(name, user_name, password)
        self.teaching_courses = []

    def create_course(self, name, code):
        course = Course(name, code, self)
        self.teaching_courses.append(course)
        return course

    def list_courses(self):
        return self.teaching_courses

    def view_course(self, course_code):
        for course in self.teaching_courses:
            if course.code == course_code:
                return course
        return None

    def create_assignment(self, course_code, title, description, due_date):
        course = self.view_course(course_code)
        if course:
            assignment = Assignment(title, description, due_date, course)
            course.assignments.append(assignment)
            return assignment
        return None

class Course:
    def __init__(self, name, code, doctor: Doctor):
        self.name = name
        self.code = code
        self.doctor = doctor
        self.students = []
        self.assignments = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def add_assignment(self, title, description, due_date):
        assignment = Assignment(title, description, due_date, self)
        self.assignments.append(assignment)
        return assignment

    def remove_assignment(self, assignment):
        self.assignments.remove(assignment)

    def list_assignments(self):
        return self.assignments

class Assignment:
    def __init__(self, title, description, due_date, course: Course):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.course = course
        self.submissions = []

    def add_solution(self, solution):
        self.submissions.append(solution)

    def list_solutions(self):
        return self.submissions

class AssignmentSolution:
    def __init__(self, student, assignment, solution):
        self.student = student
        self.assignment = assignment
        self.submission_date = "today"  
        self.grade = None
        self.comments = ""
        self.solution = solution

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def set_comment(self, comment):
        self.comments = comment

# Dummy data for testing
doctors = [
    Doctor("ali", "pass", "Dr. Ali"),
    Doctor("mostafa", "pass", "Dr. Mostafa"),
    Doctor("hani", "pass", "Dr. Hani"),
    Doctor("mohamed", "pass", "Dr. Mohamed"),
    Doctor("ashraf", "pass", "Dr. Ashraf"),
    Doctor("samy", "pass", "Dr. Samy"),
    Doctor("morad", "pass", "Dr. Morad"),
    Doctor("sayed", "pass", "Dr. Sayed"),
    Doctor("hussien", "pass", "Dr. Hussien")
]


students = [
    Student("hussien_samy", "pass", "Hussien Samy", "00102345", "hussien.samy@example.com"),
    Student("ashraf_sayed", "pass", "Ashraf Sayed", "00204690", "ashraf.sayed@example.com"),
    Student("mostafa_hussien", "pass", "Mostafa Hussien", "00307035", "mostafa.hussien@example.com"),
    Student("ali_mohamed", "pass", "Ali Mohamed", "00409380", "ali.mohamed@example.com"),
    Student("hani_sayed", "pass", "Hani Sayed", "00501725", "hani.sayed@example.com")
]

courses = [
    doctors[5].create_course("Prog 1", "CS111"),
    doctors[6].create_course("Prog 2", "CS112"),
    doctors[4].create_course("Math 1", "CS123"),
    doctors[2].create_course("Math 2", "CS333"),
    doctors[7].create_course("Prog 3", "CS136"),
    doctors[8].create_course("Stat 1", "CS240"),
    doctors[6].create_course("Stat 2", "CS350")
]


def register_students_in_courses(student, course_codes):
    for code in course_codes:
        for course in courses:
            if course.code == code:
                student.register_course(course)
                break


register_students_in_courses(students[0], ["CS111", "CS112", "CS333", "CS136", "CS240", "CS350"])
register_students_in_courses(students[1], ["CS111", "CS112", "CS123", "CS333", "CS136", "CS240", "CS350"])
register_students_in_courses(students[2], ["CS112", "CS123", "CS333", "CS136"])
register_students_in_courses(students[3], ["CS111", "CS112", "CS123", "CS333", "CS136", "CS350"])
register_students_in_courses(students[4], ["CS111", "CS112", "CS123", "CS333", "CS136", "CS240"])


def register_students_in_courses(student, course_codes):
    for code in course_codes:
        for course in courses:
            if course.code == code:
                student.register_course(course)
                break

register_students_in_courses(students[0], ["CS111", "CS112", "CS333", "CS136", "CS240", "CS350"])
register_students_in_courses(students[1], ["CS111", "CS112", "CS123", "CS333", "CS136", "CS240", "CS350"])
register_students_in_courses(students[2], ["CS112", "CS123", "CS333", "CS136"])
register_students_in_courses(students[3], ["CS111", "CS112", "CS123", "CS333", "CS136", "CS350"])
register_students_in_courses(students[4], ["CS111", "CS112", "CS123", "CS333", "CS136", "CS240"])

def main_menu():
    print("Welcome to the Educational Management System")
    print("1. Sign In")
    print("2. Sign Up")
    print("3. Exit")
    choice = input("Choose an option: ")
    return choice

def sign_in():
    username = input("Username: ")
    password = input("Password: ")
    for user in doctors + students:
        if user.user_name == username and user.password == password:
            return user
    print("\n Invalid credentials! \n")
    return None

def sign_up():
    role = input("Enter role (Doctor/Student): ")
    if role.lower() == 'doctor':
        user_name = input("Username: ")
        password = input("Password: ")
        name = input("Full Name: ")
        doctor = Doctor(user_name, password, name)
        doctors.append(doctor)
        print("\n Doctor signed up successfully!\n")
    elif role.lower() == 'student':
        user_name = input("Username: ")
        password = input("Password: ")
        name = input("Full Name: ")
        student_id = input("Student ID: ")
        email = input("Email: ")
        student = Student(user_name, password, name, student_id, email)
        students.append(student)
        print("\n Student signed up successfully!\n")
    else:
        print("\n Invalid role!\n")

def doctor_menu(doctor):
    while True:
        print(f"\nWelcome Dr. {doctor.name}\n")
        print("1. List Courses")
        print("2. Create Course")
        print("3. View Course")
        print("4. Log out")
        choice = input("Choose an option: ")

        if choice == '1':
            courses = doctor.list_courses()
            if not courses:
                print("\n No courses found.\n")
            else:
                for course in courses:
                    print(f"\n {course.name} ({course.code}) \n")

        elif choice == '2':
            name = input("Course Name: ")
            code = input("Course Code: ")
            doctor.create_course(name, code)
            print("\n Course created successfully! \n")
        elif choice == '3':
            course_code = input("Enter Course Code: ")
            course = doctor.view_course(course_code)
            if course:
                course_menu(course)
            else:
                print("\n Course not found! \n")
        elif choice == '4':
            break

def course_menu(course):
    while True:
        print(f"\n Course: {course.name} ({course.code}) \n")
        print("1. List Assignments")
        print("2. Create Assignment")
        print("3. View Assignment")
        print("4. Back")
        choice = input("Choose an option: ")

        if choice == '1':
            assignments = course.list_assignments()
            for assignment in assignments:
                print(f"{assignment.title} (Due: {assignment.due_date})")
        elif choice == '2':
            title = input("Assignment Title: ")
            description = input("Assignment Description: ")
            due_date = input("Due Date: ")
            course.add_assignment(title, description, due_date)
            print("\nAssignment created successfully!")
        elif choice == '3':
            assignment_title = input("\n Enter Assignment Title: ")
            for assignment in course.assignments:
                if assignment.title == assignment_title:
                    assignment_menu(assignment)
                    break
            else:
                print("\n Assignment not found!")
        elif choice == '4':
            break

def assignment_menu(assignment):
    while True:
        print(f"\nAssignment: {assignment.title}")
        print("1. Show Info")
        print("2. Show Grades Report")
        print("3. List Solutions")
        print("4. View Solution")
        print("5. Back")
        choice = input("Choose an option: ")

        if choice == '1':
            print(f"Title: {assignment.title}")
            print(f"Description: {assignment.description}")
            print(f"Due Date: {assignment.due_date}")
        elif choice == '2':
            for solution in assignment.submissions:
                print(f"{solution.student.name}: {solution.grade}")
        elif choice == '3':
            solutions = assignment.list_solutions()
            for solution in solutions:
                print(f"{solution.student.name}: {solution.solution}")
        elif choice == '4':
            student_name = input("Enter Student Name: ")
            for solution in assignment.submissions:
                if solution.student.name == student_name:
                    solution_menu(solution)
                    break
            else:
                print("Solution not found!")
        elif choice == '5':
            break

def solution_menu(solution):
    while True:
        print(f"\nSolution by: {solution.student.name}")
        print("1. Show Info")
        print("2. Set Grade")
        print("3. Set a Comment")
        print("4. Back")
        choice = input("Choose an option: ")

        if choice == '1':
            print(f"Content: {solution.solution}")
            print(f"Grade: {solution.grade}")
            print(f"Comment: {solution.comments}")
        elif choice == '2':
            grade = input("Enter Grade: ")
            solution.set_grade(grade)
            print("Grade set successfully!")
        elif choice == '3':
            comment = input("Enter Comment: ")
            solution.set_comment(comment)
            print("Comment set successfully!")
        elif choice == '4':
            break

def student_menu(student):
    while True:
        print(f"\nWelcome {student.name} \n")
        print("1. Register in Course")
        print("2. List My Courses")
        print("3. View a Course")
        print("4. Grades Report")
        print("5. Log out")
        choice = input("Choose an option: ")

        if choice == '1':
            register_in_course(student)
        elif choice == '2':
            list_my_courses(student)
        elif choice == '3':
            view_course(student)
        elif choice == '4':
            grades_report(student)
        elif choice == '5':
            break

def register_in_course(student):
    available_courses = [course for course in courses if student not in course.students]
    print("\nAvailable Courses:")
    for idx, course in enumerate(available_courses):
        print(f"{idx+1}. {course.name} ({course.code})")

    course_choice = int(input("Choose a course to register in: ")) - 1
    if 0 <= course_choice < len(available_courses):
        student.register_course(available_courses[course_choice])
        print("Registered successfully!")
    else:
        print("Invalid choice. Please try again.")

def list_my_courses(student):
    print("\nMy Courses:")
    for course in student.list_courses():
        print(f"{course.name} ({course.code})")

def view_course(student):
    course_code = input("Enter Course Code: ")
    course = student.view_course(course_code)
    if course:
        print(f"\nCourse: {course.name} ({course.code})")
        print("Assignments:")
        for assignment in course.assignments:
            print(f"{assignment.title} - Submitted: {'Yes' if any(sol.student == student for sol in assignment.submissions) else 'No'}")
        while True:
            print("\n1. Submit Assignment Solution")
            print("2. Unregister from Course")
            print("3. Back")
            choice = input("Choose an option: ")

            if choice == '1':
                submit_assignment_solution(student, course)
            elif choice == '2':
                unregister_from_course(student, course)
                break
            elif choice == '3':
                break
    else:
        print("Course not found!")

def grades_report(student):
    print("\nGrades Report:")
    for course in student.list_courses():
        total_assignments = len(course.assignments)
        total_grade = sum(solution.grade for assignment in course.assignments for solution in assignment.submissions if solution.student == student and solution.grade is not None)
        print(f"{course.code} - Total {total_assignments} assignments - Grade {total_grade} / {total_assignments * 100}")

def submit_assignment_solution(student, course):
    assignment_title = input("Enter Assignment Title: ")
    for assignment in course.assignments:
        if assignment.title == assignment_title:
            content = input("Enter Assignment Solution: ")
            solution = AssignmentSolution(student, assignment, content)
            assignment.add_solution(solution)
            print("Solution submitted successfully!")
            return
    print("Assignment not found!")

def unregister_from_course(student, course):
    if course in student.registered_courses:
        student.registered_courses.remove(course)
        course.students.remove(student)
        print("Unregistered successfully!")
    else:
        print("You are not registered in this course.")

# Main program loop
def main():
    while True:
        choice = main_menu()
        if choice == '1':
            user = sign_in()
            if user:
                if isinstance(user, Doctor):
                    doctor_menu(user)
                elif isinstance(user, Student):
                    student_menu(user)
        elif choice == '2':
            sign_up()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
