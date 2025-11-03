groupmates = [
    {
        "name": "Дарья",
        "surname": "Никитина",
        "exams": ["Информатика", "ОС", "КТП"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "Web", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Алексей",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Мария",
        "surname": "Сидорова",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 4]
    }
]

def print_students(students):
    print(u"Имя".ljust(15),
          u"Фамилия".ljust(12),
          u"Экзамены".ljust(35),
          u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15),
              student["surname"].ljust(12),
              str(student["exams"]).ljust(35),
              str(student["marks"]).ljust(20))

def get_avg_mark(student):
    marks = student["marks"]
    return sum(marks) / len(marks)

def filter_students_by_avg(students):
    try:
        needed_avg = float(input("Введите средний балл, от которого показывать студентов: "))
    except ValueError:
        print("Ошибка: введите число!")
        return

    good_students = []
    for student in students:
        if get_avg_mark(student) >= needed_avg:
            good_students.append(student)

    if good_students:
        print("\nСтуденты со средним баллом ≥", needed_avg)
        print_students(good_students)
    else:
        print("\nНет студентов с таким средним баллом.")

if __name__ == "__main__":
    print("Полный список студентов:\n")
    print_students(groupmates)
    print("\n--------------------------------------------\n")
    filter_students_by_avg(groupmates)
