import pandas as pd

data = {
    "BatteryCapacity": [40, 50, 60, 75, 80],
    "MotorPower": [100, 120, 150, 180, 200],
    "Range": [250, 300, 350, 420, 450],
    "ChargingTime": [6.5, 7.0, 7.5, 8.0, 8.5]
}

df = pd.DataFrame(data)

print("Column Names:")
print(df.columns)

print("Shape:")
print(df.shape)