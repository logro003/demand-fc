
from app import config

from demand_forecasting.read import read_data
from demand_forecasting.verify import verify_ride_df, verify_weather_df
from demand_forecasting.preprocess import preprocessing
from demand_forecasting.features import generate_features
from demand_forecasting.train import training_xgb_model
from demand_forecasting.features import generate_features_for_inference
from demand_forecasting.predict import predict


def main():

    # # #  Read input data  # # #
    raw_data_path = config.DATA_CONFIG['input_data_path']
    rides_raw_df = read_data(f"{raw_data_path}voiholm.csv")
    weather_raw_df = read_data(f"{raw_data_path}weather_data.csv")

    # # #  Verify dataframes # # #
    rides_df = verify_ride_df(rides_raw_df)
    weather_df = verify_weather_df(weather_raw_df)

    # # #  Preprocess input data   # # #
    processed_df, unique_h3index_df = preprocessing(rides_df=rides_df, weather_df=weather_df)

    # # #  Create features  # # #
    df_with_features = generate_features(processed_df)

    # # #  Training the model  # # #
    target = config.MODEL_CONFIG['target']
    features = config.MODEL_CONFIG['features']
    max_depth = config.MODEL_CONFIG['max_depth']
    learning_rate = config.MODEL_CONFIG['learning_rate']
    n_estimators = config.MODEL_CONFIG['n_estimators']

    model = training_xgb_model(df_with_features=df_with_features,
                                target_variable=target,
                                features=features,
                                max_depth=max_depth,
                                learning_rate=learning_rate,
                                n_estimators=n_estimators
                                )

    # # #  Making predictions for next day  # # #
    inference_with_features_df = generate_features_for_inference(unique_h3index_df, processed_df, weather_df) 
    prediction_output_df = predict(inference_with_features_df=inference_with_features_df,
                                   features=features,
                                   model=model)

    # # #  Saving prediction to output folder  # # #
    raw_data_path = config.DATA_CONFIG['output_data_path']
    prediction_output_df.to_csv(f"{raw_data_path}predictions.csv", index=False)

    return prediction_output_df