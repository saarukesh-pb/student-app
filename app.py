def show_menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

students = []
while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        students.appemd(name)
        print("Student added successfully.")

    elif choice == "2":
        print("\nStudent List:")
        for s in students:
            print("-", s)
            
    elif choice == "3":
        print("Existing application.")
        break

    else:
        print("Invalid choice.")