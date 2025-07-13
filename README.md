# BBT3101 CAT 1 - Python Programming Assignment

## Assignment Overview

This repository contains solutions to three Python programming questions for BBT3101 CAT 1, focusing on object-oriented programming concepts and interactive system development.

### Questions Covered:
1. **Library Management System (10 marks)**
   - Book and LibraryMember classes
   - Interactive borrowing and returning system
   - Kenyan literature and names
2. **Online Course Management (10 marks)**
   - Student and Instructor classes
   - Grade management and assignment tracking
   - Interactive course administration
3. **Employee and Department Management (10 marks)**
   - Employee and Department classes
   - Salary management and expenditure tracking
   - Company-wide reporting system

---

## Question 1: Library Management System

### Features Implemented:
- **Book Class**: Title, author, borrowing status
- **LibraryMember Class**: Member details and borrowed books tracking
- **Interactive Interface**: Menu-driven system for borrowing/returning books
- **Kenyan Context**: Local authors and names used throughout

### Key Methods:
- `mark_as_borrowed()` / `mark_as_returned()` in Book class
- `borrow_book()` / `return_book()` / `list_borrowed_books()` in LibraryMember class
- Input validation and error handling

### Sample Books:
- "Weep Not, Child" by Ngugi wa Thiong'o
- "The River and the Source" by Margaret Ogola
- "Petals of Blood" by Ngugi wa Thiong'o

### Sample Members:
- Wanjiku Muthoni (M001)
- Kiprop Chelimo (M002)
- Amina Hassan (M003)

### Usage:
```bash
python 112409_q1.py
```

---

## Question 2: Online Course Management

### Features Implemented:
- **Student Class**: Name, ID, assignments dictionary
- **Instructor Class**: Course management and student tracking
- **Grade Management**: Assignment grading and average calculations
- **Interactive System**: Menu-driven course administration

### Key Methods:
- `add_assignment_grade()` / `display_grades()` in Student class
- `add_student()` / `assign_grade()` / `display_all_students_grades()` in Instructor class
- Class statistics and performance tracking

### Sample Students:
- Grace Wanjiku (CS001)
- David Kiprop (CS002)
- Fatuma Said (CS003)
- John Mwangi (CS004)

### Usage:
```bash
python 112409_q2.py
```

---

## Question 3: Employee and Department Management

### Features Implemented:
- **Employee Class**: Name, ID, salary management
- **Department Class**: Employee management and expenditure tracking
- **Company Class**: Multi-department management
- **Interactive System**: Comprehensive HR management interface

### Key Methods:
- `display_details()` / `update_salary()` in Employee class
- `add_employee()` / `calculate_total_salary()` / `display_all_employees()` in Department class
- Company-wide statistics and reporting

### Sample Employees:
- Peter Kamau (EMP001) - KSh 120,000
- Mary Njeri (EMP002) - KSh 95,000
- James Otieno (EMP003) - KSh 110,000

### Sample Departments:
- Information Technology
- Human Resources
- Finance
- Marketing

### Usage:
```bash
python 112409_q3.py
```

---

## Technical Requirements

### Prerequisites:
- Python 3.6 or higher
- No external libraries required (uses built-in Python modules only)

### File Structure:
```
BBT3101_CAT1/
├── README.md
├── 112409_q1.py
├── 112409_q2.py
├── 112409_q3.py

```

---
