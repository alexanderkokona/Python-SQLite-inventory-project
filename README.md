# Inventory Management System (Python + SQLite)

## Project Description

This project demonstrates how to build software that interacts with a SQL relational database using Python and SQLite. The program allows users to manage inventory by adding, viewing, updating, and deleting product records stored in a database.

The application runs in the terminal and uses SQL queries to manipulate stored data.

---

## Features

The software meets all 5 required objectives:

1. Create a SQL database with at least one table
2. Query data from the database
3. Add new data to the database
4. Update data from the database
5. Delete data from the database

Stretch Challenge completed:

Uses aggregate SQL functions to summarize numerical data.

---

## Database Structure

Table: products

| Column | Type |
|--------|------|
| id | INTEGER (Primary Key) |
| name | TEXT |
| quantity | INTEGER |
| price | REAL |
| created_at | TEXT |

---

## How to Run

Step 1: Clone repository

git clone https://github.com/yourusername/inventory-sql-project.
git


Step 2: Navigate to folder


cd inventory-sql-project


Step 3: Run program


python main.py


---

## Example SQL Queries Used

Create table:


CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
quantity INTEGER,
price REAL
);


Insert data:


INSERT INTO products (name, quantity, price)
VALUES ("Keyboard", 5, 49.99);


Query data:


SELECT * FROM products;


Update data:


UPDATE products
SET quantity = 10
WHERE id = 1;


Delete data:


DELETE FROM products
WHERE id = 1;


Aggregate functions:


SELECT
SUM(quantity * price),
AVG(price)
FROM products;


---

## Demonstration Video

Explain:

• how the database is created  
• how records are added  
• how records are updated  
• how records are deleted  
• how SQL queries interact with the database  

---

## What I Learned

Through this project I learned:

• how relational databases store structured data  
• how SQL queries manipulate data  
• how Python connects to SQLite databases  
• how CRUD operations work in real applications  
• how aggregate functions summarize stored data  

---

## Future Improvements

Possible improvements include:

• adding multiple tables
• adding user login system
• exporting reports to CSV
• adding search functionality
• creating graphical interface

---

## Author

Alexander Kokona