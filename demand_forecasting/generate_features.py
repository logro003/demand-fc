import pandas as pd
import logging


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
    logging.info("Generating features")

    return df_with_added_features


