student_grades = {}

while True:
    print("\nMenu:")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter student name: ")
        if name in student_grades:
            print(f"{name} already exists with grade {student_grades[name]}. Use option 2 to update.")
        else:
            grade = input("Enter student grade: ")
            student_grades[name] = grade
            print(f"Added {name} with grade {grade}.")

    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in student_grades:
            grade = input("Enter new grade: ")
            student_grades[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print(f"{name} not found. Use option 1 to add them.")

    elif choice == '3':
        if not student_grades:
            print("No students in the list.")
        else:
            print("\nStudent Grades:")
            for name, grade in student_grades.items():
                print(f"{name}: {grade}")

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
