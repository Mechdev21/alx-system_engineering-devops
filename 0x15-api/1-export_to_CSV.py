#!/usr/bin/python3
"""
place holder
"""

import requests
import sys
import csv

def get_employee_todo_progress(employee_id):
    # Fetch user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return
    
    user_data = user_response.json()
    employee_name = user_data.get('name')
    username = user_data.get('username')
    
    # Fetch todos for the user
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    
    if todos_response.status_code != 200:
        print(f"Could not retrieve TODOs for user with ID {employee_id}.")
        return
    
    todos_data = todos_response.json()
    
    # Calculate number of done tasks and total tasks
    done_tasks = [todo for todo in todos_data if todo.get('completed')]
    total_tasks = len(todos_data)
    number_of_done_tasks = len(done_tasks)
    
    # Print the employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    
    for task in done_tasks:
        print(f"\t {task.get('title')}")
    
    # Export data to CSV
    csv_filename = f"{employee_id}.csv"
    
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        for task in todos_data:
            writer.writerow([employee_id, username, task.get('completed'), task.get('title')])
    
    print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)
