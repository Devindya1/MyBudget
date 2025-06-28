CREATE DATABASE MyBudget;
USE MyBudget;

-- create tables
DROP TABLE IF EXISTS Category;
CREATE TABLE Category (
  category_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR (255)
);

DROP TABLE IF EXISTS Expense; 
CREATE TABLE Expense(
  expense_id INT AUTO_INCREMENT PRIMARY KEY,
  category_id INT,
  description VARCHAR (255),
  amount DECIMAL (10,2),
  expense_date DATE,
  FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

select * from Expense