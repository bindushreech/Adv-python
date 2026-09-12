import pandas as pd

data = {
    "SensorID": ["S001", "S002", "S003", "S004", "S005"],
    "Temperature": [23.5, 24.1, 22.8, 25.3, 24.7],
    "Humidity": [56.2, 58.7, 54.5, 60.1, 57.9],
    "Pressure": [1013, 1012, 1014, 1012, 1013]
}

df = pd.DataFrame(data)

print(df[["Temperature", "Humidity", "Pressure"]].describe())