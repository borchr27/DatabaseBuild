# Give credit where credit is due https://www.youtube.com/watch?v=pd-0G0MigUA
import sqlite3
from employee import Employee

# Import file or in memory (':memory:') database (fresh clean database on every run)
#conn = sqlite3.connect('employee.db')
conn = sqlite3.connect(':memory:')

c = conn.cursor()

#Creates db table
c.execute("""CREATE TABLE employees (
    first text,
    last text,
    pay integer
    )""")

def insert_emp(emp):
    with conn: #closes the connection w the db when finished
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""", {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last", {'first': emp.first, 'last': emp.last})

# Pyhton objects not yet inserted into the database
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 87000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95700)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

conn.close()

def notes():
    """
    # Manual code to modify db
    c.execute("INSERT INTO employees VALUES (?,?,?)", (emp_1.first, emp_1.last, emp_1.pay))
    conn.commit()

    c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
    conn.commit()

    # Insert data statement
    c.execute("INSERT INTO employees VALUES ('Corey', 'Schafer', 47000)")

    # Looking for employee in database
    c.execute("SELECT * FROM employees WHERE last=?", ('Schafer',))
    print(c.fetchall())

    c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})
    print(c.fetchall())

    conn.commit()
    conn.close()
    """

