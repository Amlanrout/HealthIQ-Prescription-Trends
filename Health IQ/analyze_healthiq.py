import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',              # 🛠️ Replace with your MySQL username
    password='Connect_2024', # 🛠️ Replace with your MySQL password
    database='healthiq'       # ✅ Make sure this database exists
)

print("✅ Connected to MySQL successfully!")

# Always good to close it (for now)
conn.close()

#“Top 5 Most Prescribed Drugs”

import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Connect_2024',
    database='healthiq'
)

# Query: Top 5 most prescribed drugs
query = """
SELECT dr.brand_name AS drug_name, COUNT(*) AS times_prescribed
FROM prescriptions p
JOIN drugs dr ON p.drug_id = dr.drug_id
GROUP BY dr.brand_name
ORDER BY times_prescribed DESC
LIMIT 5;
"""

# Load data into pandas DataFrame
df = pd.read_sql(query, conn)

# Show results
print("\nTop 5 Most Prescribed Drugs:")
print(df)

# Close connection
conn.close()

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Connect_2024',
    database='healthiq'
)

# Query: Top 5 most prescribed drugs
query = """
SELECT dr.brand_name AS drug_name, COUNT(*) AS times_prescribed
FROM prescriptions p
JOIN drugs dr ON p.drug_id = dr.drug_id
GROUP BY dr.brand_name
ORDER BY times_prescribed DESC
LIMIT 5;
"""

# Load data into pandas DataFrame
df = pd.read_sql(query, conn)

# Close connection
conn.close()

# Show results
print("\nTop 5 Most Prescribed Drugs:")
print(df)

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(df['drug_name'], df['times_prescribed'], color='skyblue')
plt.title('Top 5 Most Prescribed Drugs')
plt.xlabel('Drug Name')
plt.ylabel('Number of Prescriptions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


query3 = """
SELECT d.name AS doctor_name, COUNT(*) AS prescriptions_count
FROM prescriptions p
JOIN doctors d ON p.doctor_id = d.doctor_id
GROUP BY d.name
ORDER BY prescriptions_count DESC
LIMIT 5;
"""
df3 = pd.read_sql(query3, conn)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(df3['doctor_name'], df3['prescriptions_count'], color='coral')
plt.title('Top 5 Prescribing Doctors')
plt.xlabel('Doctor Name')
plt.ylabel('Number of Prescriptions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


query4 = """
SELECT dr.category, COUNT(*) AS total_prescriptions
FROM prescriptions p
JOIN drugs dr ON p.drug_id = dr.drug_id
GROUP BY dr.category
ORDER BY total_prescriptions DESC;
"""
df4 = pd.read_sql(query4, conn)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(df4['category'], df4['total_prescriptions'], color='purple')
plt.title('Prescriptions by Drug Category')
plt.xlabel('Drug Category')
plt.ylabel('Number of Prescriptions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Reconnect to DB for next query
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Connect_2024',
    database='healthiq'
)

# Monthly Revenue Trend
query2 = """
SELECT DATE_FORMAT(month, '%Y-%m') AS month_label, SUM(sales_value) AS total_revenue
FROM sales
GROUP BY month_label
ORDER BY month_label;
"""
df2 = pd.read_sql(query2, conn)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df2['month_label'], df2['total_revenue'], marker='o', color='green')
plt.title('Monthly Drug Sales Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 5 Doctors by Number of Prescriptions
query3 = """
SELECT d.name AS doctor_name, COUNT(*) AS prescription_count
FROM prescriptions p
JOIN doctors d ON p.doctor_id = d.doctor_id
GROUP BY d.name
ORDER BY prescription_count DESC
LIMIT 5;
"""
df3 = pd.read_sql(query3, conn)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(df3['doctor_name'], df3['prescription_count'], color='salmon')
plt.title('Top 5 Doctors by Prescription Count')
plt.xlabel('Doctor Name')
plt.ylabel('Number of Prescriptions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Regional Sales Distribution
query4 = """
SELECT region, SUM(sales_value) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;
"""
df4 = pd.read_sql(query4, conn)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(df4['region'], df4['total_sales'], color='mediumseagreen')
plt.title('Total Drug Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales (₹)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plotting Monthly Sales Trend
plt.figure(figsize=(12, 6))
plt.plot(df5['sales_month'], df5['total_revenue'], marker='o', color='tomato', linestyle='-')
plt.title('Monthly Drug Sales Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Total Revenue (₹)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Top 5 doctors by number of prescriptions
query6 = """
SELECT d.name AS doctor_name, COUNT(*) AS total_prescriptions
FROM prescriptions p
JOIN doctors d ON p.doctor_id = d.doctor_id
GROUP BY d.name
ORDER BY total_prescriptions DESC
LIMIT 5;
"""
df6 = pd.read_sql(query6, conn)

# Step 6: Regional Sales Analysis
query7 = """
SELECT region, SUM(sales_value) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;
"""

# Run query and load results into DataFrame
df7 = pd.read_sql(query7, conn)

# Display results
print("\nRegional Sales Analysis:")
print(df7)

# Plot the result
plt.figure(figsize=(10, 6))
plt.bar(df7['region'], df7['total_sales'], color='coral')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 7: Monthly Sales Trend Analysis
query8 = """
SELECT DATE_FORMAT(month, '%Y-%m') AS month, 
       SUM(sales_value) AS total_revenue
FROM sales
GROUP BY month
ORDER BY month;
"""

# Execute query
df8 = pd.read_sql(query8, conn)

# Display results
print("\nMonthly Sales Trend:")
print(df8)

# Plot the result
plt.figure(figsize=(12, 6))
plt.plot(df8['month'], df8['total_revenue'], marker='o', linestyle='-', color='green')
plt.title('Monthly Sales Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 8: Doctor Specialty vs Prescription Count
query9 = """
SELECT d.specialty, COUNT(*) AS total_prescriptions
FROM prescriptions p
JOIN doctors d ON p.doctor_id = d.doctor_id
GROUP BY d.specialty
ORDER BY total_prescriptions DESC;
"""

# Execute query
df9 = pd.read_sql(query9, conn)

# Display results
print("\nDoctor Specialty vs Prescription Count:")
print(df9)

# Plot the result
plt.figure(figsize=(12, 6))
plt.bar(df9['specialty'], df9['total_prescriptions'], color='orange')
plt.title('Prescription Count by Doctor Specialty')
plt.xlabel('Doctor Specialty')
plt.ylabel('Number of Prescriptions')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Bonus Insight 1: Regional Sales Comparison
query10 = """
SELECT region, SUM(sales_value) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;
"""

df10 = pd.read_sql(query10, conn)

print("\nTotal Sales Revenue by Region:")
print(df10)

# Plot the result
plt.figure(figsize=(10, 6))
plt.bar(df10['region'], df10['total_revenue'], color='seagreen')
plt.title('Total Sales Revenue by Region')
plt.xlabel('Region')
plt.ylabel('Revenue (INR)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Bonus Insight 2: Avg Sales Value Per Prescription
query11 = """
SELECT AVG(s.sales_value) / COUNT(DISTINCT p.prescription_id) AS avg_value_per_prescription
FROM prescriptions p
JOIN sales s ON p.drug_id = s.drug_id;
"""

df11 = pd.read_sql(query11, conn)
print("\nAverage Sales Value Per Prescription:")
print(df11)


# Bonus Insight 3: Monthly Revenue Trend
query12 = """
SELECT DATE_FORMAT(month, '%Y-%m') AS month,
       SUM(sales_value) AS monthly_revenue
FROM sales
GROUP BY month
ORDER BY month;
"""

df12 = pd.read_sql(query12, conn)

print("\nMonthly Revenue Trend:")
print(df12)

# Line plot
plt.figure(figsize=(10, 6))
plt.plot(df12['month'], df12['monthly_revenue'], marker='o', linestyle='-', color='crimson')
plt.title('Month-on-Month Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


