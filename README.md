# Person, Employee & Manager Management System

A menu-driven Python console application demonstrating **Object-Oriented Programming (OOP)** through three types of records: `Person`, `Employee`, and `Manager`.

## Features

- **Create a Person** — enter a person's name and age.
- **Create an Employee** — enter the name, age, employee ID, and salary.
- **Create a Manager** — enter the name, age, employee ID, salary, and department.
- **Show Details** — choose which type of details to display:
  - Person Details
  - Employee Details
  - Manager Details
- **Exit** — leave the program and display the exit message.

## OOP Concepts

The program is intended to demonstrate common OOP ideas, including:

- **Classes and objects:** represent people, employees, and managers.
- **Inheritance:** employee and manager records can extend the common person information.
- **Encapsulation:** keep related data and behavior together in classes.
- **Methods:** create and display object details.

*The screenshots document the program's visible menu and sample interactions. They do not show the source code, so the exact class implementation should be confirmed from the Python files.*

## Requirements

- Python 3.x
- No external packages are indicated by the screenshots.

## How to Run

1. Save the Python source file(s) in your project folder.
2. Open a terminal or Command Prompt in that folder.
3. Run the main Python file:

   ```bash
   python main.py
   ```

   Replace `main.py` with the actual filename if your main file has a different name.

## Menu Preview

The program displays this main menu:

```text
Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit
```

## Screenshots

### 1. Create a Person

![Create a Person](screenshots/01-create-person.png)

### 2. Create an Employee

![Create an Employee](screenshots/02-create-employee.png)

### 3. Create a Manager

![Create a Manager](screenshots/03-create-manager.png)

### 4. Show Details

![Show Details menu](screenshots/04-show-details-menu.png)

### 5. Exit the Program

![Exit the program](screenshots/05-exit-program.png)

## Notes

- Follow the prompts shown in the terminal to enter the requested information.
- Choose **Show Details** to select the type of record to display.
- Choose **Exit** to close the application.
