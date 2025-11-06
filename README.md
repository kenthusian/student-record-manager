# Student Record Manager

A simple **Python application** to manage student records for a school.  
Records are stored in a single CSV file (`students.csv`).  
The program supports **adding**, **viewing**, **updating**, and **deleting** student records, as well as generating a **data analytics report** using **NumPy** and **Pandas**.

---

## Project Overview

This project is divided into two parts (as per BACSE101 course requirements):

1. **Part 1 – Fundamentals:**  
   A menu-driven system for record management (`main.py`)

2. **Part 2 – Analytics:**  
   A data analytics module using NumPy and Pandas (`analytics.py`)

---

## Features

- **Add New Student** – Adds a student record with validation (unique `student_id`, non-empty fields)  
- **View Student Record** – Displays a student’s full record by ID  
- **Update Student Grades** – Modifies grades for Math, Science, and English (validated between 0–100)  
- **Delete Student Record** – Removes a record after confirmation  
- **Run Analytics Report** – Executes the analytics module to show school-wide performance insights  

---

## Quick Start / Installation

### Requirements
- Python 3.x  
- Pandas  
- NumPy  

Install dependencies using:

```bash
pip install pandas numpy
