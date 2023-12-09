import os
import pandas as pd
import logging
from dateutil.relativedelta import relativedelta


def creating_avg_num_of_rides_last_week_feature(df:pd.DataFrame)-> pd.DataFrame:

    # Adding feature of average number of rides in the area during last week
    result=[]
    for area in list(df.h3index_small.unique()):
        # extrscting only data for the area h3index_small
        area_df = df[df.h3index_small == area].copy()
        area_df['one_week_before'] = area_df.date - pd.DateOffset(weeks=1)

        # extracting avergae number of rides in the area one week before, for each date
        for row in range(0, len(area_df)):
            this_date = area_df.date.iloc[row]
            one_week_before_date = area_df.one_week_before.iloc[row]
            area_one_week_before_df = area_df[(area_df.date < this_date) & (area_df.date >= one_week_before_date)]

            if len(area_one_week_before_df) < 7:
                avg_number_of_rides_one_week_before = None

            else:
                avg_number_of_rides_one_week_before = area_one_week_before_df.num_of_rides.mean()
            result.append([area, this_date, avg_number_of_rides_one_week_before])

    avg_num_of_rides_in_area_df = pd.DataFrame(result, columns=['h3index_small', 'date', 'avg_num_rides_in_area_one_week_before'])

    return avg_num_of_rides_in_area_df


def generate_features(df:pd.DataFrame)-> pd.DataFrame:

    # Feature 1: Average number of rides in the area during last week
    avg_num_of_rides_in_area_df = creating_avg_num_of_rides_last_week_feature(df)

    # Feature X: Add more features here

    # Mergin on newly created features to main dataframe 
    df_with_added_features = pd.merge(df, avg_num_of_rides_in_area_df, on=['h3index_small', 'date'], how='left')
    logging.info("Generated features for training dataset")

    return df_with_added_features



def generate_features_for_inference(unique_h3index_df: pd.DataFrame, df:pd.DataFrame, weather_df:pd.DataFrame)-> pd.DataFrame:

    date_of_prediction = pd.to_datetime(os.environ.get('PREDICTION_DATE'))
    date_one_week_before = date_of_prediction - relativedelta(days = 7)

    #  # #  Get feature data for the date of prediction  # # #
    inference_df = unique_h3index_df[['h3index_small']].copy()
    inference_df['start_date'] = date_of_prediction
    inference_df['start_weekday'] =  inference_df.start_date.dt.day_name()
    inference_df['start_weekday'] =  inference_df.start_weekday.astype("category")

    # # #  Extracting avg num rides in each area one week before  # # #
    df_one_week_before_df = df[df.start_date >= date_one_week_before]

    avg_num_of_rides_per_area_df = df_one_week_before_df.groupby('h3index_small').agg({'num_of_rides':'mean'}).reset_index()
    avg_num_of_rides_per_area_df.rename(columns={'num_of_rides':'avg_num_rides_in_area_one_week_before'}, inplace=True)

    # Adding avg num rides in each area one week before to dataframe 
    inference_df = pd.merge(inference_df, avg_num_of_rides_per_area_df, on='h3index_small', how='left')

    # # #   Get weather forecast for next day  # # #
    # this should call an external API during night to get the weather forecast for the area for the next day. 
    # since this case doesn't provide the location of Voiholm I can't implement this now 

    # lets here assume the weather forecast we get for next day is accurate, and let's use the data we have in weather_data.csv for the 2020-08-31)

    weather_at_prediciton_date_df = weather_df[weather_df.date == date_of_prediction]

    inference_df = pd.merge(inference_df, weather_at_prediciton_date_df, left_on= 'start_date', right_on='date', how='left') 
    logging.info("Generated features for interference")

    return inference_df


