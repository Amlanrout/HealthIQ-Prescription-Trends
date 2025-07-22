# HealthIQ: Prescription Trends and Doctor Behavior Analysis

A healthcare analytics project that uncovers trends in prescription patterns, top-performing drugs, doctor behaviors, and sales insights using SQL, Python, and data visualization tools.

---

## 🧠 Project Overview

**Goal:**  
To analyze healthcare prescription data and uncover valuable insights on:
- Top prescribed drugs
- Doctor behavior
- Regional and monthly sales performance
- Prescription and diagnosis relationships

**Tools Used:**  
- MySQL for data storage and querying  
- Python (`pandas`, `matplotlib`, `mysql-connector-python`)  
- Jupyter Notebook / VS Code  
- Data visualization with Matplotlib

---

## 🗃️ Dataset Description (Mock Data)

| Table Name     | Description                                 |
|----------------|---------------------------------------------|
| `prescriptions`| Records of prescriptions written by doctors |
| `doctors`      | Doctor details including specialization     |
| `drugs`        | Drug ID, brand name, and category           |
| `patients`     | Patient demographics and diagnosis          |
| `sales`        | Sales value, region, and timestamp info     |

---

## 📊 Key Analyses and Insights

### 1. Top 5 Most Prescribed Drugs
- Query: Aggregates prescriptions per drug.
- Visualization: Bar chart showing top prescribed drugs.

### 2. Top 5 Doctors by Prescription Volume
- Identifies doctors writing the most prescriptions.

### 3. Prescription Count by Specialization
- Highlights which specializations drive prescription volumes.

### 4. Age-wise Prescription Patterns
- Segments prescriptions by patient age groups.

### 5. Most Common Diagnosis Among Patients
- Uses ICD codes or condition labels to identify top health issues.

### 6. Region-wise Sales Revenue
- Compares sales performance across different geographic regions.

### 7. Average Sales Value Per Prescription
- Indicates the revenue efficiency per prescription written.

### 8. Month-on-Month Sales Trend
- Line graph showing growth or decline in sales over time.

---

