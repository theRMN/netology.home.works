class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_finished_courses(self, course_name):
        if course_name in self.courses_in_progress:
            self.finished_courses.append(course_name)
            self.courses_in_progress.remove(course_name)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_1 = Student('Roy', 'Eman', 'male')
student_1.courses_in_progress += ['Введение в программирование']
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.add_finished_courses('Введение в программирование')

lecturer_1 = Lecturer('Some', 'Body')

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Sean', 'Paul')
reviewer_2.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Git', 10)

print(student_1.grades)

print(student_1.__dict__)
