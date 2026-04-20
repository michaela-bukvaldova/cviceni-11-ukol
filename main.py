from sorting import random_numbers
from student_grades import StudentsGrades

results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print("Počet studentů:", results.count())
    for i in range(results.count()):
        body = results.get_by_index(i)
        znamka = results.get_grade(i)
        print(f"student {i}: {body} points - {znamka}")
    print("studenti se 100:", results.find(100))
    print("seřazené výsledky:", results.get_sorted())



if __name__ == "__main__":
    main()
