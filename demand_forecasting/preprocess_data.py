import pandas as pd




def processing(rides_df:pd.DataFrame,
                       weather_df: pd.DataFrame)-> pd.DataFrame:
    
    rides_df['start_date'] =  pd.to_datetime(rides_df.start_time.dt.date)
    rides_df['start_weekday'] =  rides_df.start_time.dt.day_name()

    merged_df = pd.merge(rides_df, weather_df, left_on='start_date', right_on='date', how='left')

    return merged_df


