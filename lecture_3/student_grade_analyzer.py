students = []

def student_exists(names):
    for student in students:
        if student["name"].lower() == names.lower():
            return True
    return False

while True:
    print("--- Student Grade Analyzer ---")
    menu_options = ["Add a new student", "Add grades for a student",
                    "Generates a full report", "Find the top performer", "Exit program"]
    for i, option in enumerate(menu_options, start = 1):
        print (f"{i}. {option}")
    choice_input = input("Enter your choice: ")
    try:
        choice_num = int(choice_input)
        if choice_num < 1 or choice_num > 5:
            print("Error: number must be 1-5")
            continue
    except ValueError:
        print("Invalid input. Please enter a number")
        continue

    if choice_num == 1:
        new_users_name = (input("Enter student name: ")).strip().title()
        if student_exists(new_users_name):
            print(f"Error: Student '{new_users_name}' already exists")
        else:
            new_student = {"name":new_users_name, "grades":[]}
            students.append(new_student)

    elif choice_num == 2:
        student_name = input("Enter student name: ")
        if student_exists(student_name):
            for student in students:
                if student["name"].lower() == student_name.lower():
                    while True:
                        student_grade_input = input("Enter a grade (or 'done' to finish): ")
                        if student_grade_input.lower() == 'done':
                            break
                        else:
                            try:
                                student_grade = int(student_grade_input)
                                if student_grade < 0 or student_grade > 100:
                                    print("Error: number must be 0-100")
                                    continue
                                student["grades"].append(student_grade)
                            except ValueError:
                                print("Invalid input. Please enter a number")
        else:
            print("Error: student not found")
            continue

    elif choice_num == 3:
        if not students:
            print('No students are available')
            continue
        averages = []
        print("--- Student Report ---")
        for student in students:
            name = student["name"]
            grades = student["grades"]

            try:
                average = sum(grades) / len(grades)
                print(f"{name}'s average grade is {average:.1f}")
                averages.append(average)
            except ZeroDivisionError:
                print(f"{name}'s average grade is N/A")
        if averages:
            max_average = max(averages)
            min_average = min(averages)
            overall_average = sum(averages)/len(averages)
            print("---------------------")
            print(f"Max Average: {max_average:.1f}")
            print(f"Min Average: {min_average:.1f}")
            print(f"Overall Average: {overall_average:.1f}")

    elif choice_num == 4:
        if not students:
            print("No students are available")
            continue
        students_with_grades = [s for s in students if s["grades"]]
        if not students_with_grades:
            print("No students with grades available.")
            continue
        top_student = max(students_with_grades, key=lambda student: sum(student["grades"]) / len(student["grades"]))
        top_average = sum(top_student["grades"]) / len(top_student["grades"])
        print(f"The student with the highest average rate is {top_student["name"]} with a grade of {top_average:.1f}.")

    elif choice_num == 5:
        break