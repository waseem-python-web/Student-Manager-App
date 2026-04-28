Student = {}

while True:
    print("===== Student Manager App Waseem =====")
    print("1. Add name")
    print("2. View students")
    print("3. Check result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        marks = int(input("Enter your marks: "))

        if marks < 0 or marks > 100:
            print("Invalid marks! Enter between 0-100")
            continue

        Student[name] = marks
        print(f"{name} added successfully")

    elif choice == "2":
        if not Student:
            print("No students added")
        else:
            for name, marks in Student.items():
                print(name, ":", marks)

    elif choice == "3":
        name = input("Enter your name: ")
        if name in Student:
            marks = Student[name]
            if marks >= 40:
                print("Pass")
            else:
                print("Fail")
        else:
            print("Student not found")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid  your choice")
