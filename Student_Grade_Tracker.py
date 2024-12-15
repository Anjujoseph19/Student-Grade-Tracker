# Student Grade Tracker

def calculate_letter_grade(average):
    """Determine the letter grade based on the average."""
    if average >= 90:
        return 'A', 4.0
    elif average >= 80:
        return 'B', 3.0
    elif average >= 70:
        return 'C', 2.0
    elif average >= 60:
        return 'D', 1.0
    else:
        return 'F', 0.0

def main():
    """Main function to run the grade tracker program."""
    print("\nWelcome to the Student Grade Tracker!")

    grades = {}
    while True:
        subject = input("Enter the subject (or type 'done' to finish): ").strip()
        if subject.lower() == 'done':
            break

        try:
            grade = float(input(f"Enter the grade for {subject}: ").strip())
            if grade < 0 or grade > 100:
                print("Grade must be between 0 and 100. Try again.")
                continue
            grades[subject] = grade
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    if not grades:
        print("No grades entered. Exiting program.")
        return

    total = sum(grades.values())
    count = len(grades)
    average = total / count

    letter_grade, gpa = calculate_letter_grade(average)

    print("\nGrade Summary:")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")

    print(f"\nOverall Average: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.2f}")

if __name__ == "__main__":
    main()
