def get_marks():
    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)
    return marks

def calculate_average(marks):
    return sum(marks) / len(marks)

def assign_grade(average):
    if average >= 85:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 55:
        return 'C'
    elif average >= 40 :
        return 'D'
    else:
        return 'F'

def main():
    marks = get_marks()
    average = calculate_average(marks)
    grade = assign_grade(average)

    print(f"\nAverage Marks: {average:.2f}")
    print(f"Grade: {grade}")

main()

