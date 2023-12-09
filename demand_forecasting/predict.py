import pandas as pd

def predict(inference_with_features_df: pd.DataFrame, features:list, model):

    # Preparing data for modelling - not including days when we don't have 7 days of historical data 
    predict_df = inference_with_features_df[features]

    predictions = model.predict(predict_df)

    inference_with_features_df['predictions'] = predictions

    # Forcing negative predictions to be 0
    inference_with_features_df['predictions'] = inference_with_features_df.predictions.map(lambda x: 0 if x < 0 else x)
    inference_with_features_df['prediced_num_of_rides'] = round(inference_with_features_df.predictions, 0)

    # Extracting output data 
    predicitons_output_df = inference_with_features_df[['h3index_small', 'date', 'prediced_num_of_rides']]

    return predicitons_output_df