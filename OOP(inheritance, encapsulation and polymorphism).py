class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)

    def add_finished_courses(self, course_name):
        if course_name in self.courses_in_progress:
            self.finished_courses.append(course_name)
            self.courses_in_progress.remove(course_name)

    def rate_lectures(self, lecturer, course, l_name, grade):
        if isinstance(lecturer, Lecturer) and (course in lecturer.courses_attached and
                                               course in self.courses_in_progress):
            if course in lecturer.grades:
                if l_name in lecturer.grades[course]:
                    lecturer.grades[course][l_name] += [grade]
                else:
                    lecturer.grades[course][l_name] = [grade]
            else:
                lecturer.grades.setdefault(course, {l_name: [grade]})

        else:
            print('Ошибка')

    def calculating_av_grade(self):
        avg_list = []

        for grade in self.grades.values():
            avg_list += grade

        av_grades = sum(avg_list) / len(avg_list)
        return round(av_grades, 1)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_courses_attached(self, course_name):
        self.courses_attached.append(course_name)


class Lecturer(Mentor):
    def __init__(self, *args):
        Mentor.__init__(self, *args)
        self.grades = {}

    def calculating_av_grade(self):
        avg_list = []

        for l_grades in self.grades.values():
            for grade in l_grades.values():
                avg_list += grade

        av_grades = sum(avg_list) / len(avg_list)
        return round(av_grades, 1)


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
student_1.add_courses_in_progress('Введение в программирование')
student_1.add_courses_in_progress('Python')
student_1.add_courses_in_progress('Git')
student_1.add_finished_courses('Введение в программирование')


student_2 = Student('Elis', 'Smith', 'female')
student_2.add_courses_in_progress('Введение в программирование')
student_2.add_courses_in_progress('Python')
student_2.add_finished_courses('Введение в программирование')

lecturer_1 = Lecturer('Some', 'Body')
lecturer_1.add_courses_attached('Python')

lecturer_2 = Lecturer('Some', 'Body')
lecturer_2.add_courses_attached('Git')


reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.add_courses_attached('Python')

reviewer_2 = Reviewer('Sean', 'Paul')
reviewer_2.add_courses_attached('Git')

reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Git', 4)

student_1.rate_lectures(lecturer_1, 'Python', 'lecture_1', 7)
student_1.rate_lectures(lecturer_1, 'Python', 'lecture_2', 5)
student_1.rate_lectures(lecturer_1, 'Python', 'lecture_3', 9)

student_2.rate_lectures(lecturer_1, 'Python', 'lecture_1', 9)
student_2.rate_lectures(lecturer_1, 'Python', 'lecture_2', 2)
student_2.rate_lectures(lecturer_1, 'Python', 'lecture_3', 6)

# print(student_1.calculating_av_grade())
print(lecturer_1.calculating_av_grade())

# print(student_1.grades)
# print(lecturer_1.grades)
# print(reviewer_1.__dict__)
# print(reviewer_2.__dict__)
# print(lecturer_1.__dict__)
