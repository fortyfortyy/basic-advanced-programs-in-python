class Student:
    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        if not new_grade.isdigit() or new_grade < 0 or new_grade > 100:
            raise ValueError('Value error raised')
        self._grade = new_grade

    @staticmethod
    def calculate_average_grade(students):
        grades = 0
        len_students = len(students)
        if len_students < 1:
            return -1

        for student in students:
            grades += student.grade

        return grades / len_students

    @classmethod
    def get_average_grade(cls):
        students = cls.all_students
        return cls.calculate_average_grade(students)

    @classmethod
    def get_best_student(cls):
        if len(cls.all_students) < 1:
            return
        students = sorted(cls.all_students, key=lambda student: student.grade)
        return students[::-1][0]


student1 = Student('Anton', 74)
student2 = Student('Anton', 72)
student3 = Student('Anton', 77)

