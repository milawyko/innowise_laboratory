from typing import List, Dict, Optional

students: List[Dict[str, str or List[int]]] = []


def student_exists(student_name: str) -> bool:
    return any(student["name"].lower() == student_name.lower() for student in students)


def find_student(student_name: str) -> Optional[Dict]:
    return next((s for s in students if s["name"].lower() == student_name.lower()), None)


def calculate_average(grades: List[int]) -> Optional[float]:
    return sum(grades) / len(grades) if grades else None


def get_valid_grade() -> Optional[int]:
    grade_input = input("Enter a grade (or 'done' to finish): ")
    if grade_input.lower() == 'done':
        return None

    try:
        grade = int(grade_input)
        return grade if 0 <= grade <= 100 else None
    except ValueError:
        print("Invalid input. Please enter a number")
        return None


def add_new_student() -> None:
    new_student_name = input("Enter student name: ").strip().title()

    if student_exists(new_student_name):
        print(f"Error: Student '{new_student_name}' already exists")
        return

    students.append({"name": new_student_name, "grades": []})
    print(f"Student '{new_student_name}' added successfully")


def add_grades_to_student() -> None:
    student_name = input("Enter student name: ").strip().title()
    student = find_student(student_name)

    if not student:
        print("Error: student not found")
        return

    while True:
        grade = get_valid_grade()
        if grade is None:  # User entered 'done'
            break
        student["grades"].append(grade)
        print(f"Grade {grade} added successfully")


def generate_report() -> None:
    """Generate comprehensive student report."""
    if not students:
        print('No students are available')
        return

    averages = []
    print("--- Student Report ---")

    # используем map для вычисления средних
    student_averages = list(map(lambda s: calculate_average(s["grades"]), students))

    for student, avg in zip(students, student_averages):
        name = student["name"]
        if avg is not None:
            print(f"{name}'s average grade is {avg:.1f}")
            averages.append(avg)
        else:
            print(f"{name}'s average grade is N/A")

    if averages:
        max_avg = max(averages)
        min_avg = min(averages)
        overall_avg = sum(averages) / len(averages)

        print("---------------------")
        print(f"Max Average: {max_avg:.1f}")
        print(f"Min Average: {min_avg:.1f}")
        print(f"Overall Average: {overall_avg:.1f}")


def find_top_performer() -> None:
    if not students:
        print("No students are available")
        return

    students_with_grades = list(filter(lambda s: s["grades"], students))

    if not students_with_grades:
        print("No students with grades available.")
        return

    top_student = max(students_with_grades, key=lambda s: calculate_average(s["grades"]))
    top_average = calculate_average(top_student["grades"])

    print(f"The student with the highest average is {top_student['name']} "
          f"with a grade of {top_average:.1f}.")


def get_menu_choice() -> int:
    """Get and validate menu choice from user."""
    while True:
        choice_input = input("Enter your choice: ")
        try:
            choice_num = int(choice_input)
            return choice_num if 1 <= choice_num <= 5 else None
        except ValueError:
            print("Invalid input. Please enter a number")
            return None


def display_menu() -> None:
    """Display main menu options."""
    print("--- Student Grade Analyzer ---")
    menu_options = [
        "Add a new student",
        "Add grades for a student",
        "Generate a full report",
        "Find the top performer",
        "Exit program"
    ]

    for i, option in enumerate(menu_options, start=1):
        print(f"{i}. {option}")


def main() -> None:
    """Main program loop with menu interface."""
    while True:
        display_menu()
        choice_num = get_menu_choice()

        if choice_num is None:
            continue

        menu_actions = {
            1: add_new_student,
            2: add_grades_to_student,
            3: generate_report,
            4: find_top_performer
        }

        if choice_num == 5:
            break

        if choice_num in menu_actions:
            menu_actions[choice_num]()


if __name__ == "__main__":
    main()
