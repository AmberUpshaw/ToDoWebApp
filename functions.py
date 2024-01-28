FILEPATH = "taskslist.txt"


def get_tasks(filepath=FILEPATH):
    """Reads file and returns task list"""
    with open(filepath, "r") as f:
        tasks_func = f.readlines()
    return tasks_func


def edit_tasks(tasks_arg, filepath=FILEPATH):
    """Takes current task list and
    writes to task list file
    """
    with open(filepath, "w") as f:
        f.writelines(tasks_arg)


def print_tasks(tasks_arg):
    """Prints numbered current
    task list without line breaks
    """
    for i, task_func in enumerate(tasks_arg):
        task_func = task_func.strip('\n')
        print(f"{i + 1}. {task_func}")

if __name__ == "__main__":
    print("Hello")
    print(get_tasks())