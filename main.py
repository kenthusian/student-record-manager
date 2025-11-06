import csv
import os
import analytics

FILENAME = 'students.csv'
HEADER = ['student_id', 'student_name', 'class_section', 'math_grade', 'science_grade', 'english_grade']

def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(HEADER)
        print(f"Created '{FILENAME}' with headers.")

def get_all_student_ids():
    ids = set()
    try:
        with open(FILENAME, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                ids.add(row[0])
    except FileNotFoundError:
        pass
    return ids

def add_student():
    print("\n--- Add New Student ---")
    
    existing_ids = get_all_student_ids()
    
    while True:
        student_id = input("Enter Student ID(eg: 1001): ").strip()
        if student_id in existing_ids:
            print(f"Error: Student ID '{student_id}' already exists. Please use a unique ID.")
            choise = input("Do you want to continue entering the Student ID(y/n): ").strip().lower()
            if choise == "y":
                pass
            elif choise == "n":
                return None
            else:
                print("Please enter a valid character")
        elif student_id == "":
            print("Error: Student ID cannot be empty.")
        else:
            break
            
    student_name = input("Enter Student Name: ").strip()
    class_section = input("Enter Class Section (e.g., 10-A): ").strip()
    
    math_grade = get_grade_input("Enter Math Grade: ")
    science_grade = get_grade_input("Enter Science Grade: ")
    english_grade = get_grade_input("Enter English Grade: ")

    new_row = [student_id, student_name, class_section, math_grade, science_grade, english_grade]
    
    with open(FILENAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_row)
        
    print(f"Success: Student '{student_name}' (ID: {student_id}) added.")

def get_grade_input(prompt):
    while True:
        try:
            grade = int(input(prompt))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Error: Grade must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")

def view_student():
    print("\n--- View Student Record ---")
    search_id = input("Enter Student ID to view: ").strip()
    
    try:
        with open(FILENAME, 'r', newline='') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    header = row
                    continue
                
                if row[0] == search_id:
                    print("\nStudent Found:")
                    for j in range(len(header)):
                        print(f"  {header[j].replace('_', ' ').title()}: {row[j]}")
                    return
            
            print(f"Error: Student with ID '{search_id}' not found.")
            
    except FileNotFoundError:
        print(f"Error: '{FILENAME}' not found. No students to view.")

def update_grades():
    print("\n--- Update Student Grades ---")
    search_id = input("Enter Student ID to update: ").strip()
    
    rows = []
    found = False
    
    try:
        with open(FILENAME, 'r', newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        for i in range(1, len(rows)):
            if rows[i][0] == search_id:
                print(f"Found Student: {rows[i][1]} (Class: {rows[i][2]})")
                print(f"Current Grades: Math={rows[i][3]}, Science={rows[i][4]}, English={rows[i][5]}")
                
                rows[i][3] = get_grade_input("Enter New Math Grade: ")
                rows[i][4] = get_grade_input("Enter New Science Grade: ")
                rows[i][5] = get_grade_input("Enter New English Grade: ")
                
                found = True
                break
        
        if not found:
            print(f"Error: Student with ID '{search_id}' not found.")
            return

        with open(FILENAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
            
        print("Success: Grades updated.")

    except FileNotFoundError:
        print(f"Error: '{FILENAME}' not found. No students to update.")

def delete_student():
    print("\n--- Delete Student Record ---")
    search_id = input("Enter Student ID to delete: ").strip()
    
    rows = []
    found = False
    
    try:
        with open(FILENAME, 'r', newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        new_rows = [rows[0]]
        for i in range(1, len(rows)):
            if rows[i][0] == search_id:
                found = True
                print(f"Found Student: {rows[i][1]}. This record will be deleted.")
            else:
                new_rows.append(rows[i])
        
        if not found:
            print(f"Error: Student with ID '{search_id}' not found.")
            return
        
        confirm = input("Are you sure you want to delete this student? (y/n): ").lower()
        if confirm == 'y':
            with open(FILENAME, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(new_rows)
            print("Success: Student record deleted.")
        else:
            print("Operation cancelled.")

    except FileNotFoundError:
        print(f"Error: '{FILENAME}' not found.")

def main_menu():
    initialize_file()
    
    while True:
        print("\n== Welcome to Student Record Manager ==")
        print("  Part 1: Record Management of class 10")
        print("    1. Add New Student")
        print("    2. View Student Record")
        print("    3. Update Student Grades")
        print("    4. Delete Student Record")
        print("  --------------------------------")
        print("  Part 2: Data Analytics")
        print("    5. Run School Analytics Report")
        print("  --------------------------------")
        print("    0. Exit")
        
        choice = input("Enter your choice (0-5): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            update_grades()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            analytics.run_analytics_report()
        elif choice == '0':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

if __name__ == "__main__":
    main_menu()
