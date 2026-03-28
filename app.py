import streamlit as st
import json
import os

# File to store tasks
DB_FILE = "tasks_db.json"

def load_tasks():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DB_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# UI Config
st.set_page_config(page_title="Smart Task Manager", page_icon="✅")

def main():
    st.title("✅ Smart To-Do Manager")
    st.markdown("---")

    # Load existing tasks
    if 'tasks' not in st.session_state:
        st.session_state.tasks = load_tasks()

    # --- Sidebar: Add New Task ---
    st.sidebar.header("➕ Add New Task")
    with st.sidebar.form("task_form", clear_on_submit=True):
        new_task = st.text_input("Task Description:")
        priority = st.selectbox("Priority:", ["Low", "Medium", "High"])
        submitted = st.form_submit_button("Add Task")

        if submitted and new_task:
            task_obj = {"title": new_task, "priority": priority, "done": False}
            st.session_state.tasks.append(task_obj)
            save_tasks(st.session_state.tasks)
            st.sidebar.success("Task Added!")

    # --- Main Area: Display Tasks ---
    st.subheader("Your Tasks")
    
    if not st.session_state.tasks:
        st.info("No tasks yet. Use the sidebar to add some!")
    else:
        # Create a copy for iteration to allow deletion
        for idx, task in enumerate(st.session_state.tasks):
            col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
            
            # Checkbox for status
            is_done = col1.checkbox("Done", value=task['done'], key=f"check_{idx}", label_visibility="collapsed")
            if is_done != task['done']:
                st.session_state.tasks[idx]['done'] = is_done
                save_tasks(st.session_state.tasks)
                st.rerun()

            # Task text with strike-through if done
            label = f"**[{task['priority']}]** {task['title']}"
            if task['done']:
                col2.markdown(f"~~{label}~~")
            else:
                col2.write(label)

            # Delete Button
            if col3.button("🗑️", key=f"del_{idx}"):
                st.session_state.tasks.pop(idx)
                save_tasks(st.session_state.tasks)
                st.rerun()

    # --- Metrics (For Report Reflection) ---
    st.markdown("---")
    completed = len([t for t in st.session_state.tasks if t['done']])
    total = len(st.session_state.tasks)
    if total > 0:
        progress = completed / total
        st.write(f"**Progress:** {completed}/{total} tasks completed")
        st.progress(progress)

if __name__ == "__main__":
    main()
