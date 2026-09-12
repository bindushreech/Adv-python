import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Priya", "Kiran", "Neha"],
    "Branch": ["CSE", "ECE", "ME", "CSE", "EEE"],
    "Marks": [85, 78, 92, 88, 76],
    "CGPA": [8.5, 7.8, 9.2, 8.8, 7.6]
}

df = pd.DataFrame(data)

df.info()