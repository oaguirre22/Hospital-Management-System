# Hospital Management System

Hospital Management System in Python is an advanced tool designed to automate and optimize key administrative processes in a hospital setting. It manages patient data, doctor assignments, medical histories, appointment scheduling, and system notifications using efficient data structures and algorithms.

## Project Overview

This project was developed as part of the **Data Structures II** course to demonstrate the practical application of advanced data structures. It simulates a hospital environment and provides real-time solutions for managing essential tasks in healthcare.

## Project Features

### Patient Management  
Stores, searches, and deletes patient records using hash maps. Each patient is uniquely identified and can be searched via exact ID or pattern-matching algorithms.

### Doctor Management  
Stores doctor data, specializations, and assigned patients. Uses hash maps and sets to ensure fast access and prevent duplicates.

### Appointment Scheduling  
Appointments are prioritized using a priority queue to ensure urgent cases are handled first. A FIFO queue simulates the flow of appointments.

### Medical History  
Manages patient medical histories using deques, allowing fast access to the most recent records.

### Notifications  
Handles system notifications using a simple queue (FIFO) to display reminders or updates in order of arrival.

### Reports and Statistics  
Generates reports such as:
- Number of patients per specialty
- Patients sharing specific allergies
- Top 3 patients with the most visits

### Data Persistence  
All data is saved and retrieved from text files. The system ensures that data persists across sessions and supports CSV export.

### Interactive Console UI  
Includes menus, dynamic navigation, and ASCII animations using the `colorama` library to enhance the user experience.

## Data Structures Used

- **Hash Maps**: For storing and searching patients, doctors, and medical records in constant time.
- **Priority Queues**: For sorting medical appointments by urgency.
- **Deques**: For accessing recent and historical medical records efficiently.
- **Queues**: For managing notifications in FIFO order.
- **Sets**: For storing allergies and specialties while avoiding duplicates.

## Algorithms Implemented

- **KMP (Knuth-Morris-Pratt)**: For searching patterns in names and descriptions.
- **Heap-based Priority Management**: For ordering appointments.
- **Report Generators**: For analyzing stored data and generating statistical summaries.

## How It Works

1. Data is loaded from text files at startup.
2. Users navigate via an interactive menu.
3. Modules (patients, doctors, appointments, etc.) execute operations using efficient structures.
4. Data is saved automatically before exit.

## System Requirements

- Python 3.9+
- Works on Windows, macOS, and Linux
- Required libraries: `colorama`, `os`, `random`

## Sample Use Cases

### Register a Patient
- Input: ID, full name, age, allergies
- Stored in a hash map
- Output: Confirmation and summary display

### Schedule an Appointment
- Input: Patient ID, Doctor ID, description, priority level
- Added to a priority queue
- Output: Success message and queue position

### Generate Reports
- Input: User selects a report
- Output: Data printed in the console

## Limitations

- Text-file based storage (no concurrent access or transaction handling)
- Console-based UI (no GUI)
- Limited scalability for massive datasets
- No authentication or user access control
- Spanish-only interface

## Future Improvements

- Add inventory and medication tracking
- Upgrade to a graphical interface or web version
- Use a database (e.g., SQLite or PostgreSQL) for better data management
- Add user authentication and multi-language support
