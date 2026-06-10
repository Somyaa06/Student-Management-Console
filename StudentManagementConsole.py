# Student Management System

students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == '1':
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        students[roll] = {
            "Name": name,
            "Marks": marks
        }

        print("Student added successfully!")

    # View Students
    elif choice == '2':
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for roll, info in students.items():
                print("Roll No:", roll)
                print("Name:", info["Name"])
                print("Marks:", info["Marks"])
                print("----------------------")

    # Search Student
    elif choice == '3':
        roll = input("Enter Roll Number to Search: ")

        if roll in students:
            print("Student Found:")
            print("Name:", students[roll]["Name"])
            print("Marks:", students[roll]["Marks"])
        else:
            print("Student not found.")

    # Delete Student
    elif choice == '4':
        roll = input("Enter Roll Number to Delete: ")

        if roll in students:
            del students[roll]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    # Exit
    elif choice == '5':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")