import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="raksharoot",
    database="watertech_db"
)

cursor = conn.cursor()

cursor.execute("SELECT SUM(total_amount) FROM sales_orders")
revenue = cursor.fetchone()[0]

cursor.execute("SELECT SUM(amount) FROM expenses")
expenses = cursor.fetchone()[0]

profit = revenue - expenses

print("------ BUSINESS ANALYTICS REPORT ------")
print("Total Revenue:", revenue)
print("Total Expenses:", expenses)
print("Profit:", profit)

conn.close()
