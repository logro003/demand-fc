import pandas as pd
import pandera as pa
import logging

from pandera import Column
from datetime import datetime


def verify_ride_df(df: pd.DataFrame) -> pd.DataFrame:
    table_schema = pa.DataFrameSchema(
        {
            'ride_id': Column(str, coerce=True), # coerce = True: coercing the column into the specified dtype
            'city_name': Column(str, coerce=True),
            'start_time': Column(datetime, coerce=True),
            'start_lon': Column(float, coerce=True),
            'start_lat': Column(float, coerce=True),
            'h3index_big': Column(str, coerce=True),
            'h3index_small':  Column(str, coerce=True),
        }
    )

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

    logging.info("Validated weather dataframe")
    
    return table_schema.validate(df, lazy=True)


def verify_preprocessed_df(df: pd.DataFrame)->pd.DataFrame():
    table_schema = pa.DataFrameSchema(
        {
            'h3index_small': Column(str, coerce=True),
            'start_date': Column(datetime, coerce=True),
            'num_of_rides': Column(int, coerce=True),
            'date': Column(datetime, coerce=True),
            'temperature': Column(float, coerce=True),
            'max_temperature': Column(float, coerce=True),
            'min_temperature': Column(float, coerce=True),
            'precipitation': Column(float, coerce=True),
            'start_weekday': Column(str, coerce=True)
        }
    )
    
    logging.info("Validated preprocessed dataframe")
    
    return table_schema.validate(df, lazy=True)