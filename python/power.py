import pandas as pd

data = {
    "Temperature": [72.3, 74.1, 69.8, 76.5, 73.2, 78.1],
    "Vibration": [0.45, 0.52, 0.48, 0.60, 0.55, 0.62],
    "RPM": [1500, 1520, 1485, 1600, 1550, 1620],
    "PowerConsumption": [12.5, 13.2, 11.8, 14.7, 13.9, 15.1]
}

df = pd.DataFrame(data)

print(df.head())