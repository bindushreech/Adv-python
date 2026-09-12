import pandas as pd

data = {
    "SensorID": ["S001", "S002", "S003"],
    "Temperature": [23.5, 24.1, 22.8],
    "Humidity": [56.2, 58.7, 54.5],
    "Pressure": [1013, 1012, 1014]
}

df = pd.DataFrame(data)

print(df.columns)