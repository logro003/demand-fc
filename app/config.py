MODEL_CONFIG = {
    'target': 'num_of_rides',
    'features': ['precipitation', 'start_weekday', 'max_temperature', 'avg_num_rides_in_area_one_week_before'],
    'max_depth': 3,
    'learning_rate': 0.1,
    'n_estimators': 100
}

DATA_CONFIG = {
    'raw_data_path': 'input/',
    'output_data_path': 'output/'
}