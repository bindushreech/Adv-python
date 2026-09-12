import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Priya", "Kiran", "Neha"],
    "Marks": [85, 78, 92, 88, 76],
    "Attendance": [90, 85, 95, 88, 80],
    "CGPA": [8.5, 7.8, 9.2, 8.8, 7.6]
}

df = pd.DataFrame(data)

print(df[["Marks", "Attendance", "CGPA"]].describe())