"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

# Подключение к БД PostgreSQL
conn = psycopg2.connect(database="north", user="postgres", password="root228!")

# Открытие курсора для выполнения операций с БД
cur = conn.cursor()

# Создание таблицы customers
cur.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id VARCHAR(5) PRIMARY KEY,
        company_name VARCHAR(100) NOT NULL,
        contact_name VARCHAR(100) NOT NULL
    )
""")

# Вставка данных из файла CSV в таблицу customers
with open('north_data/customers_data.csv') as file:
    reader = csv.reader(file)
    next(reader)  # пропускаем заголовки
    for row in reader:
        customer_id, company_name, contact_name = row
        cur.execute("""
            INSERT INTO customers (customer_id, company_name, contact_name)
            VALUES (%s, %s, %s)
        """, (customer_id, company_name, contact_name))

cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INT PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        title VARCHAR(255) NOT NULL,
        birth_date DATE,
        notes TEXT
    )
""")

# Вставка данных из файла CSV в таблицу employees
with open('north_data/employees_data.csv') as file:
    reader = csv.reader(file)
    next(reader)  # пропускаем заголовки
    for row in reader:
        employee_id, first_name, last_name, title, birth_date, notes = row
        cur.execute("""
            INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (employee_id, first_name, last_name, title, birth_date, notes))

# Создание таблицы orders
cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INT PRIMARY KEY,
        customer_id INT REFERENCES customers(customer_id) NOT NULL,
        employee_id INT REFERENCES employees(employee_id) NOT NULL,
        order_date DATE,
        ship_city varchar(50)
    )
""")

with open('north_data/orders_data.csv') as file:
    reader = csv.reader(file)
    next(reader)  # пропускаем заголовки
    for row in reader:
        order_id, customer_id, employee_id, order_date, ship_city = row
        cur.execute("""
            INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city)
            VALUES (%s, %s, %s, %s, %s)
        """, (order_id, customer_id, employee_id, order_date, ship_city))

# Комитим данные в БД
conn.commit()

# Закрываем курсор и соединение с БД
cur.close()
conn.close()
