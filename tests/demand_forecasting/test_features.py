import pandas as pd

from demand_forecasting.features import generate_features_for_training


def test_avg_num_of_rideds_one_week_before_feature():
    """ Testing feature generation for average number of rides one week before """
    # Given
    preprocessed_df = generate_mock_data()
    # When
    df_with_features = generate_features_for_training(preprocessed_df)
    # Then
    assert int(df_with_features.iloc[-1:, :].avg_num_rides_in_area_one_week_before.iloc[0])  == 10


def generate_mock_data():
    """ Generating mock data for testing """
    preprocessed_df = pd.DataFrame({'h3index_small': ['891f25a9ecbffff',
                                                        '891f25a9ecbffff',
                                                        '891f25a9ecbffff',
                                                        '891f25a9ecbffff',
                                                        '891f25a9ecbffff',
                                                        '891f25a9ecbffff',
                                                        '891f25a9ecbffff',
                                                        '891f25a9ecbffff',
                                                        ],
                                'start_date':[pd.to_datetime('2020-08-23'),
                                                pd.to_datetime('2020-08-24'),
                                                pd.to_datetime('2020-08-25'),
                                                pd.to_datetime('2020-08-26'),
                                                pd.to_datetime('2020-08-27'),
                                                pd.to_datetime('2020-08-28'),
                                                pd.to_datetime('2020-08-29'),
                                                pd.to_datetime('2020-08-30'),
                                                ],
                                'num_of_rides':[5, 10, 11, 12, 10, 14, 8, 6],
                                'date':[pd.to_datetime('2020-08-23'),
                                            pd.to_datetime('2020-08-24'),
                                            pd.to_datetime('2020-08-25'),
                                            pd.to_datetime('2020-08-26'),
                                            pd.to_datetime('2020-08-27'),
                                            pd.to_datetime('2020-08-28'),
                                            pd.to_datetime('2020-08-29'),
                                            pd.to_datetime('2020-08-30'),
                                            ],
                                'temperature': [ 14.8,15.9, 16.3, 17.5, 15.5, 13.8, 14.6, 14.8],
                                'max_temperature': [21.0, 20.8, 18.5, 18.8, 19.8, 21.2, 21.4, 18.6],
                                'min_temperature': [11.3 ,14.3, 13.2, 9.1, 12.1, 8.9, 10.1, 11.5],
                                'precipitation':[0.0, 0.0, 0.0, 0.6, 0.1, 0.0, 0.0, 0.0],
                                'start_weekday': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                                })

    return preprocessed_df