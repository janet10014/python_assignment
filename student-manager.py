import json

FILE_NAME = "grades.json"

def display_menu():
    print("\n--- Student Grade Manager ---")
    print("1. Add student grade")
    print("2. View all grades")
    print("3. Save grades to file")
    print("4. Load grades from file")
    print("5. Remove a student")
    print("6. Exit")

def add_student(students):
    """
    Prompt the user to enter a student name and grade.
    Validates input and adds it to the students dictionary.
    """
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    while True:
        try:
            grade = float(input("Enter student grade (0-100): "))
            if 0 <= grade <= 100:
                students[name] = grade
                print(f"{name}'s grade added successfully!")
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def view_students(students):
    if len(students) == 0:
        print("No student records available.")
        return

    print("\nStudent Grades:")
    total = 0
    for name, grade in students.items():
        print(f"{name} -> {grade}")
        total += grade

    average = total / len(students)
    print(f"Average Grade: {average:.2f}")

def save_to_file(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file)
    print("Grades saved successfully.")

def load_from_file():
    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
        print("Grades loaded successfully.")
        return students
    except FileNotFoundError:
        print("No saved data found.")
        return {}

def remove_student(students):
    name = input("Enter student name to remove: ").strip()
    if name in students:
        del students[name]
        print(f"{name} removed successfully.")
    else:
        print("Student not found.")

def main():
    students = load_from_file()

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue  # go back to the menu

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            save_to_file(students)
        elif choice == "4":
            students = load_from_file()
        elif choice == "5":
            remove_student(students)
        elif choice == "6":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
