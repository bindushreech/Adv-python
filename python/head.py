import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Priya", "Kiran", "Neha"],
    "Branch": ["CSE", "ECE", "ME", "CSE", "EEE"],
    "Marks": [85, 78, 92, 88, 76]
}

df = pd.DataFrame(data)

print(df.head())