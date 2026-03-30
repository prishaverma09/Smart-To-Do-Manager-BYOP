Project Documentation
For a detailed technical breakdown, including the problem statement, methodology, and testing results, please refer to the formal report:
 [Download Project Report PDF](./Project_Report_Smart_To-Do_Manager.pdf)


###  Smart To-Do Manager

A Persistent Task Prioritization System for Academic Productivity.

This project was developed as a Build Your Own Project (BYOP) for the Artificial Intelligence / Problem Solving course at **VIT Bhopal University**. It is a web-based application designed to help students manage lab records, assignments, and deadlines using priority-based logic.

---
 Application Gallery

| Dashboard Overview | Task Prioritization |
[Dashboard](./assets/screenshots/ss1.png) [Priority](./assets/screenshots/ss2.png) 
[Progress](./assets/screenshots/ss3.png) 

### Data Persistence
This project uses a local JSON database to store your tasks. 
You can view the raw data structure here: [View tasks_db.json](./tasks_db.json)

---

###  System Architecture
The application follows a modular architecture where the Streamlit Frontend interacts with a Python Logic Layer, which performs CRUD (Create, Read, Update, Delete) operations on a Local JSON Database.

- Frontend: Streamlit (Reactive UI)
- Backend: Python Logic & Dictionary Mapping
- Database: JSON (File-based Persistence)

---

### Installation & Setup
To run this project locally, ensure you have Python 3.10 or higher installed.

1. Clone the repo: `git clone <your-repo-link>`
2. Install Streamlit: `pip install streamlit`
3. Run the application: `python -m streamlit run app.py`
