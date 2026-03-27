# Smart Fitness Tracker System
from abc import ABC, abstractmethod
import json
import os

# =========================
# Abstract Class
# =========================
class Workout(ABC):
    def __init__(self, duration):
        self.duration = duration

    @abstractmethod
    def calculate_calories(self):
        pass


# =========================
# Child Classes
# =========================
class CardioWorkout(Workout):
    def calculate_calories(self):
        return self.duration * 8


class StrengthWorkout(Workout):
    def calculate_calories(self):
        return self.duration * 5


# =========================
# Fitness Tracker Class
# =========================
class FitnessTracker:
    def __init__(self):
        self.workouts = []
        self.load_data()

    def add_workout(self, workout):
        self.workouts.append(workout)

    def show_summary(self):
        if not self.workouts:
            print("No workouts recorded yet.")
            return

        total = 0
        print("\n--- Workout Summary ---")

        for i, workout in enumerate(self.workouts, start=1):
            calories = workout.calculate_calories()   # Polymorphism
            total += calories
            print(f"{i}. {workout.__class__.__name__} | Duration: {workout.duration} mins | Calories: {calories}")

        print(f"\nTotal Calories Burned: {total}")

    # =========================
    # Data Persistence
    # =========================
    def save_data(self):
        data = []
        for w in self.workouts:
            data.append({
                "type": w.__class__.__name__,
                "duration": w.duration
            })

        with open("data.json", "w") as f:
            json.dump(data, f)

    def load_data(self):
        if os.path.exists("data.json"):
            with open("data.json", "r") as f:
                data = json.load(f)

                for item in data:
                    if item["type"] == "CardioWorkout":
                        self.workouts.append(CardioWorkout(item["duration"]))
                    elif item["type"] == "StrengthWorkout":
                        self.workouts.append(StrengthWorkout(item["duration"]))


# =========================
# CLI Menu
# =========================
def menu():
    tracker = FitnessTracker()

    while True:
        print("\n===== Smart Fitness Tracker =====")
        print("1. Add Cardio Workout")
        print("2. Add Strength Workout")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                duration = int(input("Enter duration (minutes): "))
                tracker.add_workout(CardioWorkout(duration))
                print("Cardio workout added!")

            elif choice == "2":
                duration = int(input("Enter duration (minutes): "))
                tracker.add_workout(StrengthWorkout(duration))
                print("Strength workout added!")

            elif choice == "3":
                tracker.show_summary()

            elif choice == "4":
                tracker.save_data()
                print("Data saved successfully. Goodbye!")
                break

            else:
                print("Invalid choice! Please try again.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


# =========================
# Main Entry Point
# =========================
if __name__ == "__main__":
    menu()
