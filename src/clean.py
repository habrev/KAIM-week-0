#  data cleaning 

import pandas as pd
import numpy as np

def clean_data(df):
    """
    Clean the dataset by handling missing values, anomalies, and irrelevant columns.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame to be cleaned.
    
    Returns:
    - df (pd.DataFrame): The cleaned DataFrame.
    """
    # Step 1: Drop columns that are entirely null (e.g., 'Comments')
    df = df.dropna(axis=1, how='all')  # Drop columns where all values are NaN
    
    # Step 2: Handle missing values in the remaining columns
    # Fill missing numerical columns with median, and categorical columns with mode
    for column in df.columns:
        if df[column].dtype == 'object':  # Categorical data
            df[column] = df[column].fillna(df[column].mode()[0])  # Fill with mode
        else:  # Numerical data
            df[column] = df[column].fillna(df[column].median())  # Fill with median
    
    # Step 3: Handle anomalies in numerical columns (e.g., negative values where they shouldn't be)
    # Define the columns where you expect non-negative values
    columns_to_check = ['GHI', 'DNI', 'DHI', 'WS', 'WSgust', 'TModA', 'TModB']
    
    # Replace negative values in these columns with NaN (or you can choose to drop them if needed)
    for column in columns_to_check:
        if column in df.columns:
            df[column] = df[column].apply(lambda x: x if x >= 0 else np.nan)
    
    # Step 4: Drop rows with NaN after anomaly correction (optional, depending on dataset size)
    df = df.dropna(how='any')  # Drop rows where any column has NaN (optional based on dataset size)
    
    return df

# Example Usage
if __name__ == "__main__":
    # Load dataset (replace 'your_dataset.csv' with your actual file path)
    try:
        df = pd.read_csv('../assets/data/benin-malanville.csv')
    except FileNotFoundError:
        print("Error: The file 'benin-malanville.csv' was not found.")
        exit()

    # Clean the data
    df_cleaned = clean_data(df)

    # Display the cleaned data (or save it to a new file)
    print(df_cleaned.head())

    # Optionally, save the cleaned dataset to a new file
    df_cleaned.to_csv('cleaned_benin_malanville.csv', index=False)
