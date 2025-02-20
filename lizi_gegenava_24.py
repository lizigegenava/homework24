class InvalidCreditsError(Exception):
    pass


class InvalidGradeError(Exception):
    pass


class DuplicateCourseError(Exception):
    pass


import utils_grades


class Course:
    def __init__(self, name, credits, grades=None):
        self.name = name
        self.credits = int(credits)
        if self.credits != 5 and self.credits != 10:
            raise InvalidCreditsError
        self.grades = []

    def __str__(self):
        return f"Subject name: {self.name}\nCredits: {self.credits}\nGrades: {self.grades}"

    def add_grade(self, grade):
        if grade > 100 or grade < 0:
            raise InvalidGradeError
        self.grades.append(grade)

    def get_final_grade(self):
        return utils_grades.calculate_average(self.grades)


class Student:
    def __init__(self, name, courses=None):
        self.name = name
        self.courses = {}

    def __str__(self):
        return f"Name: {self.name}\nCourses: {self.courses}"

    def add_course(self, course_name, credits):
        if course_name in self.courses:
            raise DuplicateCourseError
        self.courses[course_name] = Course(course_name, credits)

    def remove_course(self, course_name):
        if course_name in self.courses:
            del self.courses[course_name]

    def get_gpa(self):
        sum_grades = sum(i.get_final_grade() * i.credits for i in self.courses.values())
        sum_credits = sum(i.credits for i in self.courses.values())
        return sum_grades / sum_credits

    def get_transcript(self):
        for i in self.courses.values():
            print("Course name: ", i.name)
            print("Credits: ", i.credits)
            print("Final grade: ", i.get_final_grade())
            print("Letter grade: ", utils_grades.grade_to_letter(i.get_final_grade()))

    def check_scholarship_eligibility(self):
        if self.get_gpa() >= 80:
            return True
        else:
            return False


student = Student("Giorgi Maisuradze")
student.add_course("Math", 10)
student.add_course("Physics", 5)

math_course = student.courses["Math"]
math_course.add_grade(85)
math_course.add_grade(92)

physics_course = student.courses["Physics"]
physics_course.add_grade(78)
physics_course.add_grade(88)

student.get_transcript()