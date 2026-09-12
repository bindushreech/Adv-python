import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Priya", "Kiran", "Neha", "Arun", "Divya"],
    "Branch": ["CSE", "ECE", "ME", "CSE", "EEE", "IT", "CSE"],
    "Marks": [85, 78, 92, 88, 76, 90, 82]
}

df = pd.DataFrame(data)

print(df.tail())