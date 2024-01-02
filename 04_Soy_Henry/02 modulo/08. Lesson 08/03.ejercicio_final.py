import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect(r'C:\Users\flore\Sqlite\northwind.db')
# vamos a hacer 3 consultas
# cual es el producto mas rentable

query = ''' 
        SELECT ProductName, SUM(Price * Quantity) AS Sales
        FROM OrderDetails OD
        JOIN Products p ON p.ProductID = OD.ProductID
        GROUP BY OD.ProductId
        ORDER BY Sales DESC 
        LIMIT 10'''
        
top_products = pd.read_sql_query(query,conn)        
top_products.plot(x="ProductName",y="Sales",kind="bar",figsize=(10,5),legend=False)
plt.title("10 Productos mas Vendidos")
plt.xlabel("Productos")
plt.ylabel("Sales")
plt.xticks(rotation=90)
plt.show()

# buscamos el empleado que mas vendio

query2 = ''' 
        SELECT FirstName || " " || LastName AS Employee, COUNT(*) AS Total
        FROM Orders o
        JOIN Employees e ON e.EmployeeId = o.EmployeeId
        GROUP BY o.EmployeeId
        ORDER BY Total DESC 
        LIMIT 10'''
        
top_employees = pd.read_sql_query(query2,conn)        
top_employees.plot(x="Employee",y="Total",kind="bar",figsize=(10,5),legend=False)
plt.title("10 empleados que mas Vendieron")
plt.xlabel("Employee")
plt.ylabel("Total")
plt.xticks(rotation=45)
plt.show()

# Vamos despedir a los 3 peores empleados. 
# Cuales son los 3 que menos vendieron

query3 = ''' 
        SELECT FirstName || " " || LastName AS Employee, COUNT(*) AS Total
        FROM Orders o
        JOIN Employees e ON e.EmployeeId = o.EmployeeId
        GROUP BY o.EmployeeId
        ORDER BY Total ASC 
        LIMIT 10'''
        
top_employees = pd.read_sql_query(query3,conn)        
top_employees.plot(x="Employee",y="Total",kind="bar",figsize=(10,5),legend=False)
plt.title("10 empleados que mas Vendieron")
plt.xlabel("Employee")
plt.ylabel("Total")
plt.xticks(rotation=45)
plt.show()
