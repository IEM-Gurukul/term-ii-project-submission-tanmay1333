# PCCCS495 – Term II Project

## Project Title
Smart Fitness Tracker System

---

## Problem Statement (max 150 words)
Maintaining a healthy lifestyle requires consistent tracking of workouts and physical activities. However, many users lack a simple and efficient system to log and analyze their fitness routines. This project aims to develop a Smart Fitness Tracker System that allows users to record workouts, calculate calories burned, and monitor progress. The system is designed using object-oriented programming principles to ensure modularity, scalability, and maintainability. It provides a lightweight and user-friendly solution for tracking fitness activities through a command-line interface.

---

## Target User
- Fitness enthusiasts  
- Students and beginners  
- Users preferring simple CLI tools  

---

## Core Features
- Add cardio and strength workouts  
- Calculate calories burned  
- View workout summary  
- Data persistence using file storage  
- Simple CLI-based interaction  

---

## OOP Concepts Used
- **Abstraction:** Abstract class `Workout`  
- **Inheritance:** `CardioWorkout`, `StrengthWorkout`  
- **Polymorphism:** Different calorie calculations  
- **Exception Handling:** Handles invalid inputs  
- **Collections:** List used to store workouts  

---

## Proposed Architecture Description
The system follows an object-oriented architecture with an abstract base class `Workout` and derived classes for different workout types. A `FitnessTracker` class manages all operations such as adding workouts, calculating calories, and storing data. The application uses file handling (JSON) for data persistence. The CLI interface enables user interaction in a simple and efficient way.

---

## How to Run
```bash
cd src
python main.py

## Git Discipline Notes
- Minimum 10 meaningful commits maintained  
- Incremental development followed  
- Proper descriptive commit messages used  
- Work distributed across multiple days  
