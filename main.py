class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


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


class Reviewer(Mentor):
    """ Класс, описывающий экспертов, которые проверяют домашние задания """

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
