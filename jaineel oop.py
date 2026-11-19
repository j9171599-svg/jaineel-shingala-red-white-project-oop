
# -----------------------------------------
# OOP PROGRAM: PERSON, EMPLOYEE AND MANAGER
# -----------------------------------------

# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("\nPerson Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Derived Class: Employee
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def show_details(self):
        print("\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")


# Derived Class: Manager
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def show_details(self):
        print("\nManager Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")
        print(f"Department: {self.department}")


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

people = []
employees = []
managers = []


def main():

    while True:

        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        # Create Person
        if choice == "1":

            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))

            person = Person(name, age)
            people.append(person)

            print(
                f"\nPerson created with name: {name}, "
                f"age: {age}."
            )

        # Create Employee
        elif choice == "2":

            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))

            employee = Employee(
                name, age, employee_id, salary
            )

            employees.append(employee)

            print(
                f"\nEmployee created with name: {name}, "
                f"age: {age}, ID: {employee_id}, "
                f"and salary: ${salary}."
            )

        # Create Manager
        elif choice == "3":

            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")

            manager = Manager(
                name, age, employee_id, salary, department
            )

            managers.append(manager)

            print(
                f"\nManager created with name: {name}, "
                f"age: {age}, ID: {employee_id}, "
                f"salary: ${salary}, "
                f"and department: {department}."
            )

        # Show Details
        elif choice == "4":

            print("\nChoose details to show:")
            print("1. Person Details")
            print("2. Employee Details")
            print("3. Manager Details")

            detail_choice = input("\nEnter your choice: ")

            if detail_choice == "1":

                if people:
                    for person in people:
                        person.show_details()
                else:
                    print("\nNo Person details available.")

            elif detail_choice == "2":

                if employees:
                    for employee in employees:
                        employee.show_details()
                else:
                    print("\nNo Employee details available.")

            elif detail_choice == "3":

                if managers:
                    for manager in managers:
                        manager.show_details()
                else:
                    print("\nNo Manager details available.")

            else:
                print("\nInvalid choice!")

        # Exit
        elif choice == "5":

            print(
                "\nExiting the system. "
                "All resources have been freed."
            )
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")

        if choice != "5":
            print("\n--- Choose another operation ---")


# Run Program
if __name__ == "__main__":
    main()
