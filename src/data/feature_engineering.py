# src/data/feature_engineering.py

import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def engineer_features (df):
    """
        Perform feature engineering on the input dataframe, including scaling features.

        Args:
        - df (pd.DataFrame): The cleaned data.

        Returns:
        - pd.DataFrame: The data with engineered features.
    """

    # Scale the features using MinMaxScaler
    scaler = MinMaxScaler()
    numerical_features = ['rainfall_mm','soil_quality_index','farm_size_hectares','sunlight_hours','fertilizer_kg','crop_yield']

    #apply scaling
    df[numerical_features] = scaler.fit_transform(df[numerical_features])


    return df


# # Test the data cleaning function
# if __name__ == "__main__":
#     df = pd.read_csv('data/processed/cleaned_crop_data.csv')
#     engineered_df = engineer_features(df)
#     engineered_df.to_csv('data/processed/engineered_crop_data.csv', index=False)
