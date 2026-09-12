import pandas as pd

data = {
    "StudentID": [101, 102, 103, 104, 105, 106, 107],
    "Name": ["Asha", "Ravi", "Priya", "Kiran", "Neha", "Arun", "Divya"],
    "Branch": ["CSE", "ECE", "ME", "CSE", "EEE", "IT", "CSE"],
    "Marks": [85, 78, 92, 88, 76, 90, 82],
    "Attendance": [90, 85, 95, 88, 80, 92, 87],
    "CGPA": [8.5, 7.8, 9.2, 8.8, 7.6, 9.0, 8.2]
}

df = pd.DataFrame(data)

print("1. HEAD - First five records:")
print(df.head())

print("\n2. TAIL - Last five records:")
print(df.tail())

print("\n3. SHAPE - Number of rows and columns:")
print(df.shape)

print("\n4. COLUMNS - Column names:")
print(df.columns)

print("\n5. INFO - Complete information:")
df.info()

print("\n6. DESCRIBE - Statistical summary:")
print(df.describe())