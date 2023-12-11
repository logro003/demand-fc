
import pandas as pd

from demand_forecasting.preprocess import preprocessing


def test_len_of_df():
    # Given
    rides_df, weather_df = generate_mock_data()
    # When
    df_preprocessed = preprocessing(rides_df, weather_df)
    # Then
    assert len(df_preprocessed) == 2
    

def test_number_of_rides():
    # Given
    rides_df, weather_df = generate_mock_data()
    # When
    df_preprocessed = preprocessing(rides_df, weather_df)
    #Then 
    assert df_preprocessed.num_of_rides.sum() == 2


def generate_mock_data():
    rides_df = pd.DataFrame({'ride_id': ['97341db7-f89f-45db-9dd1-bcc2620fc1db', '646c160f-bbb7-4c78-b2ca-bdd8644a8400'],
                                'city_name':['voiholm', 'voiholm'],
                                'start_time':[pd.to_datetime('2020-08-05 04:27:40.425797 UTC'), pd.to_datetime('2020-08-06 07:47:29.060615 UTC')],
                                'start_lon':[11.908586502075194, 11.908669471740723],
                                'start_lat':[57.6871223449707, 57.687049865722656],
                                'h3index_big':['881f250613fffff', '881f250613fffff'],
                                'h3index_small':['891f250612bffff', '891f250612bffff'],
                                })

    weather_df = pd.DataFrame({'date': [pd.to_datetime('2020-08-05'), pd.to_datetime('2020-08-06')],
                                'temperature': [15.9, 16.3],
                                'max_temperature': [18.6, 21.0],
                                'min_temperature': [14.3, 11.2],
                                'precipitation':[4.66, 0.0]
                                })
    return rides_df, weather_df
 