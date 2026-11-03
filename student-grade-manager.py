# Student Grade Manager

students = {}


# Function to calculate grade
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Function to add student
def add_student():
    name = input("Enter student name: ")

    if name in students:
        print("Student already exists!")
        return

    marks = []

    for i in range(3):
        mark = float(input(f"Enter mark for subject {i + 1}: "))

        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100!")
            return

        marks.append(mark)

    average = sum(marks) / len(marks)
    grade = calculate_grade(average)

    students[name] = {
        "marks": marks,
        "average": average,
        "grade": grade
    }

    print("Student added successfully!")


# Function to display students
def display_students():
    if not students:
        print("No student records found!")
        return

    print("\n===== Student Records =====")

    for name, details in students.items():
        print(f"\nName: {name}")
        print(f"Marks: {details['marks']}")
        print(f"Average: {details['average']:.2f}")
        print(f"Grade: {details['grade']}")


# Function to search student
def search_student():
    name = input("Enter student name to search: ")

    if name in students:
        details = students[name]

        print("\n===== Student Details =====")
        print(f"Name: {name}")
        print(f"Marks: {details['marks']}")
        print(f"Average: {details['average']:.2f}")
        print(f"Grade: {details['grade']}")
    else:
        print("Student not found!")


# Function to find topper
def find_topper():
    if not students:
        print("No student records found!")
        return

    topper = max(
        students,
        key=lambda name: students[name]["average"]
    )

    print("\n===== Topper =====")
    print(f"Name: {topper}")
    print(f"Average: {students[topper]['average']:.2f}")
    print(f"Grade: {students[topper]['grade']}")


# Main menu
while True:

    print("\n===== Student Grade Manager =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Find Topper")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        find_topper()

    elif choice == "5":
        print("Thank you for using Student Grade Manager!")
        break

    else:
        print("Invalid choice! Please try again.")