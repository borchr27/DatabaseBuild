# Give credit where credit is due https://www.youtube.com/watch?v=pd-0G0MigUA
import sqlite3
from employee import Employee

# Import file or in memory (':memory:') database (fresh clean database on every run)
conn = sqlite3.connect('employee.db')

c = conn.cursor()

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

def show_all():
    with conn:
        c.execute("SELECT * FROM employees")
    return print(c.fetchall()) 

# Pyhton objects not yet inserted into the database
emp_1 = Employee('First', 'Last', 55000)

#remove_emp(emp_1)
#insert_emp(emp_1)

#emps = get_emps_by_name('Doe')
#print(emps)

#update_pay(emp_2, 95700)
#remove_emp(emp_1)

#emps = get_emps_by_name('Doe')
#print(emps)

show_all()

conn.close()