import logging
import pandas as pd
import xgboost as xgb


def training_xgb_model(
    df_with_features: pd.DataFrame,
    target_variable: str,
    features: list,
    max_depth: int,
    learning_rate: float,
    n_estimators: int,
):
    """ Function that trains the model with model variables from model config """

    # Preparing data for modelling - not including days when we don't have 7 days of historical data
    all_feature_df = df_with_features[
        df_with_features.avg_num_rides_in_area_one_week_before.notna()
    ]

    columns = features.copy()
    columns.append(target_variable)
    model_df = all_feature_df[columns].copy()
    model_df["start_weekday"] = model_df.start_weekday.astype("category")

    X = model_df.drop(columns=target_variable)
    y = model_df[[target_variable]]

    # Fitting the model
    xgb_best_model = xgb.XGBRegressor(
        enable_categorical=True,
        max_depth=max_depth,
        learning_rate=learning_rate,
        n_estimators=n_estimators,
        objective="reg:squarederror",
        booster="gbtree",
    )
    model = xgb_best_model.fit(X, y)
    logging.info("Trained XGB model")

    return model
