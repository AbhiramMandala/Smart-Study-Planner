import json

DATA_FILE = "study_data.json"


def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return {}


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_subject(data):
    subject = input("Enter subject name: ")

    try:
        hours = int(input("Required study hours: "))
    except:
        print("Invalid input.")
        return

    data[subject] = {
        "hours": hours,
        "completed": 0
    }

    save_data(data)
    print("Subject added successfully!")


def generate_plan(data):
    if not data:
        print("No subjects found.")
        return

    daily_hours = int(input("Hours available per day: "))

    print("\n===== STUDY PLAN =====")

    for subject in data:
        hours = data[subject]["hours"]
        days = max(1, hours // daily_hours)

        print(f"{subject}")
        print(f"  Total Hours : {hours}")
        print(f"  Estimated Days : {days}")
        print()


def update_progress(data):
    if not data:
        print("No subjects found.")
        return

    print("\nSubjects:")
    subjects = list(data.keys())

    for i in range(len(subjects)):
        print(f"{i+1}. {subjects[i]}")

    choice = int(input("Select subject: ")) - 1

    if choice < 0 or choice >= len(subjects):
        print("Invalid choice.")
        return

    completed = int(input("Hours completed: "))

    subject = subjects[choice]

    data[subject]["completed"] += completed

    save_data(data)

    print("Progress updated!")


def view_statistics(data):
    total_required = 0
    total_completed = 0

    for subject in data:
        total_required += data[subject]["hours"]
        total_completed += data[subject]["completed"]

    print("\n===== STATISTICS =====")
    print(f"Total Hours Required : {total_required}")
    print(f"Total Hours Completed: {total_completed}")

    if total_required > 0:
        progress = (total_completed / total_required) * 100
        print(f"Overall Progress: {progress:.2f}%")

    print()

    for subject in data:
        print(
            f"{subject}: "
            f"{data[subject]['completed']}/"
            f"{data[subject]['hours']} hrs"
        )


def main():
    data = load_data()

    while True:
        print("\n========================")
        print(" SMART STUDY PLANNER")
        print("========================")
        print("1. Add Subject")
        print("2. Generate Study Plan")
        print("3. Update Progress")
        print("4. Statistics")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_subject(data)

        elif choice == "2":
            generate_plan(data)

        elif choice == "3":
            update_progress(data)

        elif choice == "4":
            view_statistics(data)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()
