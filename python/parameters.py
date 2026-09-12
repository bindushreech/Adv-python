import pandas as pd

data = {
    "Temperature": [72.3, 74.1, 69.8, 76.5, 73.2],
    "Vibration": [0.45, 0.52, 0.48, 0.60, 0.55],
    "RPM": [1500, 1520, 1485, 1600, 1550],
    "PowerConsumption": [12.5, 13.2, 11.8, 14.7, 13.9]
}

df = pd.DataFrame(data)

print(df.describe())