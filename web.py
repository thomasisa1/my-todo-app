import streamlit as st
import functions
from datetime import datetime



if "todos" not in st.session_state:
    st.session_state["todos"] = functions.get_todos()

def add_todo():
    """Adds a new todo item with a timestamp."""
    todo = st.session_state["new_todo"].strip()
    if todo:  # Prevent adding empty tasks
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        todo_with_timestamp = f"{todo} - {timestamp}"

        st.session_state["todos"].append(todo_with_timestamp)  # Append new task
        functions.write_todos(st.session_state["todos"])  # Save to file
        st.session_state["new_todo"] = ""  # Clear input field

# UI Elements
st.title("My Todo App")
st.subheader("This is a To-do app")
st.write("This app is to increase your productivity.")

# Collect checked todos for removal
todos_to_keep = []
for index, todo in enumerate(st.session_state["todos"]):
    checked = st.checkbox(todo, key=f"checkbox_{index}")
    if not checked:  # Keep only unchecked tasks
        todos_to_keep.append(todo)

# If any tasks were removed, update state and rerun
if len(todos_to_keep) != len(st.session_state["todos"]):
    st.session_state["todos"] = todos_to_keep
    functions.write_todos(st.session_state["todos"])
    st.rerun()  # Refresh UI after removing todos

# Add new todo item
st.text_input(label="", placeholder="Enter a todo...",
              on_change=add_todo, key="new_todo")






