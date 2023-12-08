import pandas as pd
import pandera as pa
import logging

from pandera import Column
from datetime import datetime

logging.getLogger().setLevel(logging.INFO)

def verify_ride_df(df: pd.DataFrame) -> pd.DataFrame:

    table_schema = pa.DataFrameSchema(
        {
            'ride_id': Column(str, coerce=True), # coerce = True: coercing the column into the specified dtype
            'city_name': Column(str, coerce=True),
            'start_time': Column(datetime, coerce=True),
            'start_lon': Column(float, coerce=True),
            'start_lat': Column(float, coerce=True),
            'h3index_big': Column(str, coerce=True),
        }
    )
    # get all columns with date type and fill na:
    #for col in df.select_dtypes(include=['datetime']).columns:
    #    df[col] = df[col].fillna('1970-01-01 00:00:00')
    logging.info("Validated Voiholm ride dataframe")
    
    return table_schema.validate(df, lazy=True)


def verify_weather_df(df: pd.DataFrame) -> pd.DataFrame:

    table_schema = pa.DataFrameSchema(
        {
            'date': Column(datetime, coerce=True), # coerce = True: coercing the column into the specified dtype
            'temperature': Column(float, coerce=True),
            'max_temperature': Column(float, coerce=True),
            'min_temperature': Column(float, coerce=True),
            'precipitation': Column(float, coerce=True),
        }
    )
    # get all columns with date type and fill na:
    #for col in df.select_dtypes(include=['datetime']).columns:
    #    df[col] = df[col].fillna('1970-01-01 00:00:00')
    logging.info("Validated weather dataframe")
    
    return table_schema.validate(df, lazy=True)