import pandas as pd
import random
import config

def generate_random_id():
    """Returns random 12 digit ID (str)"""
    random_id = ""
    characters = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for _ in range(12):
        random_id += random.choice(characters)
    return random_id

def read_dataframe():
    """Reads Pandas DataFrame from CSV source"""
    return pd.read_csv(config.CSV_FILEPATH)

def save_dataframe(data):
    """Saves Pandas DataFrame to CSV file"""
    return data.to_csv(config.CSV_FILEPATH, index=False)