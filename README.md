# Task Manager CLI

A simple command-line interface (CLI) application for managing a list of tasks.

## Description

This Python application allows users to add, view, and delete tasks. It's designed to be run from the terminal and provides a straightforward menu-driven interface. Tasks are stored in memory while the application is running.

## Features

- **Add Tasks:** Add new tasks to your to-do list.
  - Input validation prevents:
    - Empty tasks or tasks consisting only of whitespace.
    - Tasks containing only symbols (at least one letter or number is required).
    - Duplicate tasks (case-sensitive).
    - Tasks longer than 50 characters.
- **View Tasks:** Display all current tasks with a corresponding number.
- **Delete Tasks:** Remove tasks from the list by specifying the task name.
- **Quit:** Exit the application.

## Requirements

- Python 3.x

## How to Run

1.  Ensure you have Python 3 installed on your system.
2.  Save the application code as `taskapp.py` (or your preferred filename).
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the application using the command:
    ```bash
    python taskapp.py
    ```
6.  Follow the on-screen menu prompts to manage your tasks.