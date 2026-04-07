import pandas as pd

def create_dataframe():
    return pd.DataFrame(columns=["City", "Temperature", "Rainfall", "Humidity"])


def add_data(df, city, temp, rainfall, humidity):
    new_row = pd.DataFrame({
        "City": [city],
        "Temperature": [temp],
        "Rainfall": [rainfall],
        "Humidity": [humidity]
    })
    return pd.concat([df, new_row], ignore_index=True)