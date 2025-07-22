import pandas as pd
import mysql.connector

# ✅ MySQL connection - update these credentials
conn = mysql.connector.connect(
    host='localhost',
    user='root',       # <-- change this
    password='Connect_2024',   # <-- change this
    database='healthiq'
)
cursor = conn.cursor()

# ✅ Load CSVs (assuming they are in the same folder)
doctors = pd.read_csv('doctors.csv')
patients = pd.read_csv('patients.csv')
drugs = pd.read_csv('drugs.csv')
prescriptions = pd.read_csv('prescriptions.csv')
sales = pd.read_csv('sales.csv')

# ✅ Insert function
def insert_dataframe(df, table_name):
    cols = ",".join(df.columns)
    placeholders = ",".join(["%s"] * len(df.columns))
    sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
    for _, row in df.iterrows():
        cursor.execute(sql, tuple(row))
    conn.commit()

# ✅ Insert into MySQL
insert_dataframe(doctors, 'doctors')
insert_dataframe(patients, 'patients')
insert_dataframe(drugs, 'drugs')
insert_dataframe(prescriptions, 'prescriptions')
insert_dataframe(sales, 'sales')

cursor.close()
conn.close()
print("✅ All data inserted successfully.")


import mysql.connector
import pandas as pd

# MySQL connection settings
conn = mysql.connector.connect(
    host='localhost',
    user='root',          # replace with your MySQL username
    password='Connect_2024',  # replace with your MySQL password
    database='healthiq'
)

cursor = conn.cursor()

query = """
SELECT d.brand_name AS drug_name, COUNT(*) AS times_prescribed
FROM prescriptions p
JOIN drugs d ON p.drug_id = d.drug_id
GROUP BY d.brand_name
ORDER BY times_prescribed DESC
LIMIT 5;
"""

cursor.execute(query)
data = cursor.fetchall()

# Load into DataFrame
df = pd.DataFrame(data, columns=['Drug Name', 'Times Prescribed'])
print(df)
