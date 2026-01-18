# 💰 MyBudget – Expense Tracker

MyBudget is a full-stack expense tracking application developed as a solo project. It allows users to manage expense categories, record expenses, and view summaries grouped by category. The project is designed to demonstrate practical backend and frontend development skills using modern web technologies.

The application is being built with a React + Vite frontend and a Node.js + Express backend, using MySQL for persistent data storage.

---

## 🚀 Features

- Add and manage expense categories
- Add expenses linked to categories
- View all expenses
- View total expenses grouped by category
- RESTful API architecture
- Clean and modular backend structure
- Scalable full-stack design

---

## 🛠️ Tech Stack

**Frontend**
- React
- Vite
- JavaScript

**Backend**
- Node.js
- Express.js
- MySQL

**Database**
- MySQL
  
---

## 📦 Folder Structure

my-budget/
├── backend/
│   ├── app.js
│   ├── server.js
│   ├── config/
│   │   └── db.js
│   ├── controllers/
│   ├── routes/
│   ├── middleware/
│   ├── package.json
│   └── .env
│
├── frontend/
│   └── (React + Vite source files)
│
├── database/
│   └── schema.sql
│
└── README.md



---

## ⚙️ Setup Instructions

### 1. Clone the project or download the code:

```bash
git clone https://github.com/Devindya1/mybudget.git
cd mybudget

### 2. Create and activate a virtual environment 
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

### 3. Install required package:
pip install mysql-connector-python

### 4. Install required package:
pip install mysql-connector-python

### 5. Set Up the MySQL Database

Open **MySQL Workbench** or your MySQL CLI, and run the `MyBudget.sql` script to create the required database and tables.

If you're using Workbench:
1. Open `MyBudget.sql`.
2. Connect to your MySQL server.
3. Execute the script (⚡ Run All).

This will create:
- A database named `MyBudget`
- Two tables: `Category` and `Expense`

---

### 6. Configure Your MySQL Credentials in `config.py`

Open `config.py` in **VS Code** and update the connection details with your MySQL username and password:

```python
config = {
    'host': 'localhost',
    'user': 'your_mysql_username',
    'password': 'your_mysql_password',
    'database': 'MyBudget'
}

### 7. Run main.py 

## 🛠️ Upcoming Features

A user interface (UI) will be added in the future to improve usability — either as a simple desktop GUI using Tkinter or a web-based interface using Flask.

Thank you


🙌 Acknowledgements
Created with ❤️ using Python and MySQL.

_Future plans: A user-friendly UI will be added soon using Tkinter or Flask._
