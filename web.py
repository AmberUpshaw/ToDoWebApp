import streamlit as sl 
import functions as f
import os

# If taskslist.txt doesn't exist it gets created
if not os.path.exists("taskslist.txt"):
    with open("taskslist.txt", "w") as file:
        #creates empty
        pass

# grabs task list via get_task funtion
tasks = f.get_tasks()

# adds tasks to task list
def add_task():
    task = sl.session_state["new_task"] + "\n"
    tasks.append(task)
    f.edit_tasks(tasks)

# Title and subheader for streamlit page
sl.title("Todo List")
sl.subheader("Keep track of your activities to increase productivity")

for index, task in enumerate(tasks):
    checkbox = sl.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        f.edit_tasks(tasks) 
        del sl.session_state[task]
        #needed for checkboxes
        #automatically updates the app
        sl.experimental_rerun()      
        

sl.text_input(label="Test", label_visibility="hidden", placeholder="Add a new task...", on_change=add_task, key="new_task")