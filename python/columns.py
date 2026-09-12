import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Priya"],
    "Branch": ["CSE", "ECE", "ME"],
    "Marks": [85, 78, 92],
    "Attendance": [90, 85, 95]
}

df = pd.DataFrame(data)

print(df.columns)