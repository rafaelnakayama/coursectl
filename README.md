# Students Log (Student Management Console System)

## Overview

After almost two years giving English classes, I realized I needed a system to help me organize and track of my student progress. Each student learns different things at different times, and I needed a structured way to store what each student had already done in my course.

This program was developed entirely for my **personal use**, tailored to my workflow and the structure of my own English course (That was uploaded on Google Drive). For that reason, it is **not intended as a universal tool**, since every teacher works differently. The system solves my needs specifically.

---

## How the System Works

I have a complete English course uploaded on **Google Drive**, containing:

- Classes
- Texts  
- Exercises  

Inside the code, I use the **Google Drive API (via Google Cloud Platform)** to connect and request metadata from my Drive. The program retrieves:

- The names of each class  
- The names of texts  
- The names of exercises and other materials  
- Their file IDs

Once this information is downloaded, the program writes and updates all data into local `.csv` files. From that point onward:

- Every lesson is stored locally  
- Every student in the system can be associated with those lessons  
- When a class is assigned to a student, it means the student has watched it  
- The system keeps a general information of all students progress in `students.csv` files
- And stores each student's history inside a `historicos` dic, where each individual has three files. Example:
A person called Rafael will have a `(Rafael's ID)_exercises.csv`, `(Rafael's ID)_classes.csv` and `(Rafael's ID)_texts.csv`

Through the console interface, I can:

- Add new students  
- Remove students
- Edit basic data of a specific individual  
- Assign or remove lessons from a student  
- Store personal reminders/notes for each student  
- Review everything using formatted terminal tables

All data manipulation is local, no need to reopen Google Drive after initial sync.

---

## 🛠️ Technologies Used

The project was written in **Python** and uses:

- `pandas` – reading and manipulating `.csv` files  
- `csv` – direct writing and reading of CSV  
- `os` – file handling  
- `uuid` – unique student IDs  
- `tabulate` – formatted terminal tables  
- Google Drive API (GCP) – retrieving course metadata from the cloud  
- `PyInstaller` – packaging into a standalone executable

No online database is required. After Drive syncing, everything runs locally.

---

## 📂 Project Structure (Simplified):

