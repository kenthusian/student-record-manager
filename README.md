# Student-Record-Manager

A simple Python application to manage student records for a school. Records are stored in a single CSV  
file (`students.csv`). The code supports adding, viewing, updating, and deleting student records, plus  
a data analytics report using NumPy and Pandas.

This project is divided into two main parts:

1. **Part 1 (Fundamentals):** A menu-driven system for record management (`main.py`).  
2. **Part 2 (Analytics):** A data analytics module using NumPy and Pandas (`analytics.py`).

---

## Features

**Add New Student:** Adds a new student record with validation (unique `student_id`, non-empty fields).  

**View Student Record:** Fetches and displays a student's full record by their ID.  

**Update Student Grades:** Updates a student's Math, Science, and English grades (validated 0–100).  

**Delete Student Record:** Deletes a student record with user confirmation.  

**Run Analytics Report:** Calls the `analytics.py` module to print a comprehensive school performance report.  

---

## Quick Start / Installation

### 1. Requirements

- Python 3.x  
- Pandas  
- NumPy  

To install the required libraries, open your terminal and run:

```bash
pip install pandas numpy
```

---

### 2. Setup

1. Save the three files (`main.py`, `analytics.py`, `students.csv`) in a single project folder.  
2. Open your terminal or command prompt.  
3. Navigate to the folder where you saved the files:

```bash
cd path/to/your/project/folder
```

---

### 3. Steps to Run

1. In your terminal, run the `main.py` script:

```bash
python main.py
```

2. The application menu will appear, and you can now use the program.

---

## Usage

The code runs as an interactive menu:

```
===== Student Record Manager =====

  Part 1: Record Management
    1. Add New Student
    2. View Student Record
    3. Update Student Grades
    4. Delete Student Record
  --------------------------------
  Part 2: Data Analytics
    5. Run School Analytics Report
  --------------------------------
    0. Exit

Enter your choice (0-5):
```

---

### Prompts and Validation

**Student ID:** Must be unique. The program will check for duplicates.  
**Grades:** Must be integers between 0 and 100. Non-integer or out-of-range input is rejected.

---

## Data Storage (`students.csv`)

**File name:** `students.csv` (created automatically on the first run if missing).

**Header:**
```
student_id,student_name,class_section,math_grade,science_grade,english_grade
```

**Example Row:**
```
1001,Raj Sharma,10-A,85,90,78
```

---

## Project Structure

### main.py  
Contains the main CLI application, menu, and all record management functions  
(`add_student`, `view_student`, `update_grades`, `delete_student`).  
Uses `students.csv` for persistent storage.

### analytics.py  
Module used by `main.py` to produce the analytics output.  
Contains all NumPy and Pandas logic (e.g., `groupby`, `nlargest`, `pd.cut`).

### students.csv  
The data file used for storing student records. An example file is provided.

---

## Author

Developed by **Arav Kilak**

---

## License

This project is free to use and modify for educational or personal purposes.
