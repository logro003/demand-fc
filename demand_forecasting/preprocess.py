import os
import logging
import pandas as pd
from dateutil.relativedelta import relativedelta


def extract_all_unique_h3index_small_areas(rides_df: pd.DataFrame) -> pd.DataFrame:
    """ Function that extract all unique h3index_small areas """
    unique_h3index_df = (
        rides_df.groupby("h3index_small").count().reset_index()[["h3index_small"]]
    )
    return unique_h3index_df


def preprocessing(rides_df: pd.DataFrame, weather_df: pd.DataFrame) -> pd.DataFrame:
    """ Function which preprocess the data """
    rides_df["start_date"] = pd.to_datetime(rides_df.start_time.dt.date)

    # Getting traning date and number of histroical days to include in traning dataset
    training_date = pd.to_datetime(os.environ["TRAINING_DATE"])
    number_of_days_to_include_in_training = int(os.environ["TRAINING_NUMBER_OF_DAYS"])

    # Only extracting data for the the peiod we want to include in the training data
    date_to = training_date
    date_from = training_date - relativedelta(
        days=number_of_days_to_include_in_training + 1
    )
    rides_df = rides_df[
        (rides_df.start_date >= date_from) & (rides_df.start_date <= date_to)
    ]

    # # #  Creating a dataframe with all possible combinations of days and h3index small area  # # #
    # Extracting all unique h3index small
    unique_h3index_df = extract_all_unique_h3index_small_areas(rides_df)
    unique_h3index_df["key"] = 1

    # Extracting all uqniue dates in the dataset
    unique_dates_df = (
        rides_df.groupby("start_date").count().reset_index()[["start_date"]]
    )
    unique_dates_df["key"] = 1

    # Creating a dataframe which combines all possible combinations of days and h3index small areas
    all_combination_df = pd.merge(unique_h3index_df, unique_dates_df, on="key").drop(
        "key", axis=1
    )

    # # #    # # #
    # Aggregating number of rides per h3index_small area and per day
    rides_per_h3_and_day_df = (
        rides_df.groupby(["h3index_small", "start_date"])
        .agg({"ride_id": "nunique"})
        .reset_index()
    )
    rides_per_h3_and_day_df.rename(columns={"ride_id": "num_of_rides"}, inplace=True)

    # Merging on the dataframe with all potential combinations to be able to set rides to 0 when we dont have any rides in an area on a day
    rides_per_area_and_day_df = pd.merge(
        rides_per_h3_and_day_df,
        all_combination_df,
        on=["h3index_small", "start_date"],
        how="outer",
    )
    rides_per_area_and_day_df.num_of_rides.fillna(0, inplace=True)
    rides_per_area_and_day_df.sort_values(
        by=["h3index_small", "start_date"], inplace=True
    )
    rides_per_area_and_day_df = rides_per_area_and_day_df.reset_index().drop(
        columns="index"
    )

    # Merging on weather per day
    preprocessed_df = pd.merge(
        rides_per_area_and_day_df,
        weather_df,
        left_on="start_date",
        right_on="date",
        how="left",
    )

    # Adding ride start date and weekday to dataframe
    preprocessed_df["start_weekday"] = preprocessed_df.start_date.dt.day_name()
    logging.info("Preprossed dataframe")

    return preprocessed_df
