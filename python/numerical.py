import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Priya", "Kiran", "Neha"],
    "Python": [85, 78, 92, 88, 76],
    "DAA": [80, 75, 90, 85, 72]
}

df = pd.DataFrame(data)

print(df[["Python", "DAA"]].describe())