def home():
    return "Welcome to the Task Management Application!"

def add_task(task):
    return f"Task added successfully: {task}"

def display_tasks(tasks):
    return "\n".join(tasks)

if __name__ == "__main__":
    print(home())
