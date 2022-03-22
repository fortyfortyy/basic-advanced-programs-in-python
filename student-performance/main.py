import json
import os

NUM_STUDENTS = 1000
STUDENTS_FOLDER = './students'
SUBJECTS = ["math", "science", "history", "english", "geography"]


def load_report_card(directory, student_nb):
    # get each student from the json file
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_nb}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card


def set_average_student_grade_and_subjects_grades_total(student_report, subjects_grades_total):
    average_student_grade = 0.0

    for subject in SUBJECTS:
        average_student_grade += student_report[subject]

        if subject not in subjects_grades_total:
            subjects_grades_total[subject] = 0.0
        subjects_grades_total[subject] += student_report[subject]

    student_report['average'] = average_student_grade / len(SUBJECTS)


def set_worst_best_student_id(student_report, best_student, worst_student):
    best_student_average = 0 if best_student.get('student', 0) == 0 else best_student.get('student')[1]
    worst_student_average = 0 if worst_student.get('student', 0) == 0 else worst_student.get('student')[1]
    student_average = student_report['average']

    if 'student' not in best_student or student_average > best_student_average:
        best_student['student'] = [student_report['id'], student_report['average']]

    if 'student' not in worst_student or student_average < worst_student_average:
        worst_student['student'] = [student_report['id'], student_report['average']]


# init the variables
subjects_grades_total = {}
best_student = {}
worst_student = {}
grade_level_averages = {grade: [] for grade in range(1, 9)}
average_students_grade = []


for student_number in range(NUM_STUDENTS):
    student_report = load_report_card(STUDENTS_FOLDER, student_number)
    if not student_report:
        continue

    set_average_student_grade_and_subjects_grades_total(student_report, subjects_grades_total)
    set_worst_best_student_id(student_report, best_student, worst_student)
    grade_level_averages[student_report['grade']].append(student_report['average'])
    average_students_grade.append(student_report['average'])

average_students_grade = round(sum(average_students_grade) / NUM_STUDENTS, 2)
easiest_subject = max(subjects_grades_total, key=subjects_grades_total.get)
hardest_subject = min(subjects_grades_total, key=subjects_grades_total.get)

# sum and sort the averages on each grade
grade_level_averages = {grade: round(sum(values) / len(values), 2) for grade, values in grade_level_averages.items()}
grade_level_averages = sorted(grade_level_averages.items(), key=lambda grade: grade[1])


print("Average Student Grade:", average_students_grade)
print("Hardest Subject:", hardest_subject)
print("Easiest Subject:", easiest_subject)
print("Best Performing Grade:", grade_level_averages[-1][0])
print("Worst Performing Grade:", grade_level_averages[0][0])
print("Best Student ID:", best_student['student'][0])
print("Worst Student ID:", worst_student['student'][0])
