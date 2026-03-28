import java.util.*;

// Abstract Class
abstract class Workout {
    protected int duration;

    public Workout(int duration) {
        this.duration = duration;
    }

    public abstract int calculateCalories();
}

// Cardio Workout
class CardioWorkout extends Workout {
    public CardioWorkout(int duration) {
        super(duration);
    }

    @Override
    public int calculateCalories() {
        return duration * 8;
    }
}

// Strength Workout
class StrengthWorkout extends Workout {
    public StrengthWorkout(int duration) {
        super(duration);
    }

    @Override
    public int calculateCalories() {
        return duration * 5;
    }
}

// Fitness Tracker
class FitnessTracker {
    private List<Workout> workouts = new ArrayList<>();

    public void addWorkout(Workout workout) {
        workouts.add(workout);
    }

    public void showSummary() {
        int totalCalories = 0;

        System.out.println("\n--- Workout Summary ---");

        for (Workout w : workouts) {
            int calories = w.calculateCalories();
            totalCalories += calories;

            System.out.println(
                w.getClass().getSimpleName() +
                " | Duration: " + w.duration +
                " mins | Calories: " + calories
            );
        }

        System.out.println("Total Calories Burned: " + totalCalories);
    }
}

// Main Class
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        FitnessTracker tracker = new FitnessTracker();

        while (true) {
            System.out.println("\n===== Smart Fitness Tracker =====");
            System.out.println("1. Add Cardio Workout");
            System.out.println("2. Add Strength Workout");
            System.out.println("3. Show Summary");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");

            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter duration (minutes): ");
                    int d1 = sc.nextInt();
                    tracker.addWorkout(new CardioWorkout(d1));
                    System.out.println("Cardio workout added!");
                    break;

                case 2:
                    System.out.print("Enter duration (minutes): ");
                    int d2 = sc.nextInt();
                    tracker.addWorkout(new StrengthWorkout(d2));
                    System.out.println("Strength workout added!");
                    break;

                case 3:
                    tracker.showSummary();
                    break;

                case 4:
                    System.out.println("Exiting... Goodbye!");
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid choice!");
            }
        }
    }
}
