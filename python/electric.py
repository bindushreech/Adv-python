import pandas as pd

data = {
    "StudentID": [1, 2, 3, 4, 5, 6],
    "Math": [85, 92, 76, 88, 91, 79],
    "Science": [78, 88, 81, 85, 89, 82],
    "English": [82, 90, 79, 87, 93, 85]
}

df = pd.DataFrame(data)

print("First Five Records:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

print("\nStatistical Summary:")
print(df.describe())