# Student-Record-Manager

Simple Code to manage student records for a school class (class 10). Records are stored in a single CSV file (students.csv). The code supports adding, viewing, updating, and deleting student records, plus a data analytics report via the included analytics module, i.e, numpy and pandas.

## Features
- Add new student records with validation (unique student_id, non-empty fields).
- View a student's full record by student ID.
- Update math, science, and English grades (grades validated to be integers between 0 and 100).
- Delete student records with confirmation.
- Runs a school analytics report.

## Quick Start / Installation
1. Requirements
   - Python 
   - Install modules pandas and numpy
   - For installing the modules, open the terminal and then type pip install pandas, followed by pip install numpy. If already installed, leave it
   - After that, save the 3 files (main.py, analytics.py, students.csv) in a separate folder on your device
2. Steps to run the File
   - Open the folder in which the files are saved on your device
   - Then right click and give open in terminal, then type python main.py and then enter
   - Now the code will run

## Usage
- The code runs as an interactive menu:
  1. Add New Student
  2. View Student Record
  3. Update Student Grades
  4. Delete Student Record
  5. Run School Analytics Report
  0. Exit

## - Prompts and validation:
  - Student ID must be unique (you are prompted to retry or cancel if it exists).
  - Student name and class/section are free-text inputs.
  - Grades must be integers between 0 and 100. Non-integer input is rejected.

## Data storage (students.csv)
- File name: students.csv (created automatically on first run if missing)
- Header (CSV columns):
  student_id, student_name, class_section, math_grade, science_grade, english_grade

## - Example CSV row:
  1001,John Doe,10-A,85,78,92

## Project structure (important files)
- main.py
  - Main CLI application, menu, and all record management functions:
    - initialize_file()
    - add_student()
    - view_student()
    - update_grades()
    - delete_student()
    - main_menu()
  - Uses students.csv for persistent storage.
- analytics.py
  - Module used by main.py to produce analytics output.
  - Invoked via analytics.run_analytics_report() from the main menu.
  - (See analytics.py to review exactly which analytics are produced and how they are formatted.)
- students.csv
  - Example/data file used for the code.

##  Project Contributors
| Name | Registration Number | Role |
|------|---------------------|------|
| **Mithul Ram Sundaresan** | 25BCE2031 | Project Lead & Architect |
| **Divyam Kurkan** | 25BCE2041 | Backend Developer (Part 1 - Read/Create) |
| **Pratham Garg** | 25BCE2016 | Backend Developer (Part 1 - Update/Delete) |
| **Devanupriy Jain** | 25BCE0991 | Data Analyst (Part 2) |
| **Jaidev A** | 25BCE0971 | Quality Assurance & Documentation |

**Supervisor:** *Thirumoorthy K Sir*  
**School of Computer Science and Engineering, VIT Vellore**

## Conclusion
Student-Record-Manager is a lightweight, easy-to-use Python tool for managing class 10 student records using a CSV backend. It supports adding, viewing, updating, and deleting records and includes a simple analytics report to help summarize class performance. This project is intended for learning and small-class management; contributions, bug reports, and feature requests are welcome via issues or pull requests. Future improvements could include persistent database storage, automated tests, and a graphical or web-based interface.

##  License
This project is developed for academic and research purposes as part of the **BACSE101 – Problem Solving Using Python** course at **VIT University**.

