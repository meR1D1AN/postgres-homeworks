-- SQL-команды для создания таблиц
CREATE TABLE IF NOT EXISTS customers
(
	customer_id VARCHAR(5) PRIMARY KEY,
	company_name VARCHAR(100) NOT NULL,
	contact_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS employees
(
	employee_id INT PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	title VARCHAR(255) NOT NULL,
	birth_date DATE,
	notes TEXT
);

CREATE TABLE IF NOT EXISTS orders
(
	order_id INT PRIMARY KEY,
	customer_id VARCHAR(5) REFERENCES customers(customer_id) NOT NULL,
	employee_id INT REFERENCES employees(employee_id) NOT NULL,
	order_date DATE,
	ship_city varchar(50)
);
