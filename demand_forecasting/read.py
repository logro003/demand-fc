import sys
import pandas as pd
import logging

logging.getLogger().setLevel(logging.INFO)

# Read the CSV file into a pandas DataFrame
def read_data(file_path: str)-> pd.DataFrame:
    df = pd.read_csv(file_path)
    logging.info(f"Read dataframe from file path {file_path}")

    return df
