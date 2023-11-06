#!/usr/bin/python3
# Define an empty dictionary to store employee data
employee_database = {}

# Function to add a new employee
def add_employee():
    employee_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    job = input("Enter Job: ")
    salary = float(input("Enter Salary: "))
    
    # Check if the employee ID is already in the database
    if employee_id in employee_database:
        print("Employee with the same ID already exists.")
    else:
        employee_database[employee_id] = {"Name": name, "Job": job, "Salary": salary}
        print("Employee added successfully.")

# Function to print employee data
def print_employee_data():
    employee_id = input("Enter Employee ID to print data: ")
    if employee_id in employee_database:
        employee_info = employee_database[employee_id]
        print(f"Employee ID: {employee_id}")
        print(f"Name: {employee_info['Name']}")
        print(f"Job: {employee_info['Job']}")
        print(f"Salary: {employee_info['Salary']}")
    else:
        print("Employee not found.")

# Function to remove an employee
def remove_employee():
    employee_id = input("Enter Employee ID to remove: ")
    if employee_id in employee_database:
        del employee_database[employee_id]
        print("Employee removed successfully.")
    else:
        print("Employee not found.")

# Function to print all employee data
def print_all_employee_data():
    if employee_database:
        print("Employee Data:")
        for employee_id, employee_info in employee_database.items():
            print(f"Employee ID: {employee_id}")
            print(f"Name: {employee_info['Name']}")
            print(f"Job: {employee_info['Job']}")
            print(f"Salary: {employee_info['Salary']}")
            print()
    else:
        print("No employees in the database.")

# Function to delete all employee data
def delete_all_employee_data():
    confirm = input("Are you sure you want to delete all employee data? (yes/no): ")
    if confirm.lower() == 'yes':
        employee_database.clear()
        print("All employee data deleted.")
    else:
        print("Deletion canceled.")

# Main program loop
while True:
    print("\nEmployee Database Management System")
    print("1. Add new employee")
    print("2. Print employee data")
    print("3. Print all employee data")
    print("4. Remove employee")
    print("5. Delete all employee data")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_employee()
    elif choice == '2':
        print_employee_data()
    elif choice == '3':
        print_all_employee_data()
    elif choice == '4':
        remove_employee()
    elif choice == '5':
        delete_all_employee_data()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please select a valid option.")

print("Thank you for using the Employee Database Management System.")