class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def put_rating(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.finished_courses \
                and course in lector.courses_attached and 1 <= grade <= 10:
            if course in lector.courses_rating:
                lector.courses_rating[course] += [grade]
            else:
                lector.courses_rating[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """ Класс, описывающий лекторов. """

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.courses_rating = {}


class Reviewer(Mentor):
    """ Класс, описывающий экспертов, которые проверяют домашние задания """

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
