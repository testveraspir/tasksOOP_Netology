class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0
        list_grades = []
        for value in self.grades.values():
            for grade in value:
                list_grades.append(grade)
        return round(sum(list_grades) / len(list_grades), 1)

    def __str__(self):
        # проверка наличия оценок
        if len(self.grades) == 0:
            info_average_grades = "Оценок ещё нет!"
        else:
            info_average_grades = self.get_average_grade()
        # проверка наличия курсов в процессе обучения
        if len(self.courses_in_progress) == 0:
            info_courses_in_progress = "Курсы ещё не добавлены."
        else:
            info_courses_in_progress = ', '.join(self.courses_in_progress)
        # проверка наличия завершённых курсов
        if len(self.finished_courses) == 0:
            info_finished_courses = "Нет завершённых курсов."
        else:
            info_finished_courses = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {info_average_grades}\n" \
               f"Курсы в процессе изучения: {info_courses_in_progress}\n" \
               f"Завершённые курсы: {info_finished_courses}\n"

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

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

    def get_average_grade(self):
        if len(self.courses_rating) == 0:
            return 0
        list_rating = []
        for value in self.courses_rating.values():
            for grade in value:
                list_rating.append(grade)
        return round(sum(list_rating) / len(list_rating), 1)

    def __str__(self):
        # проверка наличия оценок
        if len(self.courses_rating) == 0:
            average_rating = "Оценок ещё нет!"
        else:
            average_rating = self.get_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {average_rating}\n"

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()


class Reviewer(Mentor):
    """ Класс, описывающий экспертов, которые проверяют домашние задания """

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
