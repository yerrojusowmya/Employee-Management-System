import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yerrojusowmya",  # change this
    database="employee_db"
)

cursor = conn.cursor()

# Add Employee
def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    dept = input("Enter department: ")
    position = input("Enter position: ")
    salary = float(input("Enter salary: "))

    query = "INSERT INTO employees (name, age, department, position, salary) VALUES (%s, %s, %s, %s, %s)"
    values = (name, age, dept, position, salary)

    cursor.execute(query, values)
    conn.commit()
    print("Employee added successfully!")

# View Employees
def view_employee():
    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()

    for row in data:
        print(row)

# Update Employee
def update_employee():
    emp_id = int(input("Enter employee ID: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    dept = input("Enter new department: ")
    position = input("Enter new position: ")
    salary = float(input("Enter new salary: "))

    query = """UPDATE employees 
               SET name=%s, age=%s, department=%s, position=%s, salary=%s 
               WHERE emp_id=%s"""
    values = (name, age, dept, position, salary, emp_id)

    cursor.execute(query, values)
    conn.commit()
    print("Employee updated successfully!")

# Delete Employee
def delete_employee():
    emp_id = int(input("Enter employee ID: "))
    cursor.execute("DELETE FROM employees WHERE emp_id=%s", (emp_id,))
    conn.commit()
    print("Employee deleted successfully!")

# Menu
def menu():
    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

menu()