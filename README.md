# 💰 MyBudget – Expense Tracker

MyBudget is a simple command-line-based expense tracking system built with Python and MySQL. It allows users to manage expense categories, add expenses, and view summaries grouped by category.

---

## 🚀 Features

- Add and manage expense categories
- Add new expenses linked to categories
- View all expenses in descending order by date
- View total expenses by category
- Clean and modular Python code
- Uses MySQL for data storage

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Database:** MySQL
- **Library:** `mysql-connector-python`

---

## 📦 Folder Structure

Mybudget
├── MyBudget.sql # MySQL script file
├── config.py # MySQL connection config
├── db.py # Database interaction logic
├── main.py # Command-line interface
└── README.md # This file


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


🙌 Acknowledgements
Created with ❤️ using Python and MySQL.

_Future plans: A user-friendly UI will be added soon using Tkinter or Flask._
