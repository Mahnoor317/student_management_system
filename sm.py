# Student Management System (CLI + File Handling)
# You can paste this code in VS Code / PyCharm / IDLE

import json
import os

FILE_NAME = "students.json"

# ---------- File Handling ----------

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


students = load_data()

# ---------- Functions ----------

def add_student():
    roll = input("Enter Roll No: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    percentage = marks / 500 * 100

    if percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    students[roll] = {
        "name": name,
        "marks": marks,
        "percentage": percentage,
        "grade": grade
    }

    save_data(students)
    print("Student Added Successfully!\n")


def view_students():
    if not students:
        print("No records found.\n")
        return

    for roll, info in students.items():
        print(f"Roll No: {roll}")
        print(f"Name: {info['name']}")
        print(f"Marks: {info['marks']}")
        print(f"Percentage: {info['percentage']:.2f}%")
        print(f"Grade: {info['grade']}")
        print("-" * 30)


def search_student():
    roll = input("Enter Roll No to Search: ")

    if roll in students:
        info = students[roll]
        print(f"Name: {info['name']}")
        print(f"Marks: {info['marks']}")
        print(f"Percentage: {info['percentage']:.2f}%")
        print(f"Grade: {info['grade']}\n")
    else:
        print("Student not found!\n")


def delete_student():
    roll = input("Enter Roll No to Delete: ")

    if roll in students:
        del students[roll]
        save_data(students)
        print("Record Deleted Successfully!\n")
    else:
        print("Student not found!\n")


# ---------- Main Menu ----------

def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Try again.\n")


# ---------- Run Program ----------
menu()
