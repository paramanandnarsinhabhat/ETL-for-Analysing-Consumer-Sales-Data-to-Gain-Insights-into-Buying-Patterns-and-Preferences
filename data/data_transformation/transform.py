import pandas as pd
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Now you can import common_utils
from utilities import common_utils

# Define the path to the CSV file
csv_file_path = '/Users/paramanandbhat/Downloads/SalesJan2009.csv'
# Call the function to read the data
sales_data = common_utils.read_csv_file(csv_file_path)

# Splitting the transform_data function into smaller, more specialized functions

def standardize_date_formats(df, columns):
    """
    Standardize the date formats for given columns.
    """
    for col in columns:
        df[col] = pd.to_datetime(df[col])
    return df

def fill_missing_values(df, fill_values):
    """
    Fill missing values in the DataFrame as per the fill_values dictionary.
    """
    for col, fill_value in fill_values.items():
        df[col] = df[col].fillna(fill_value)
    return df

def convert_text_to_lowercase(df):
    """
    Convert all text columns to lowercase.
    """
    string_columns = df.select_dtypes(include=['object']).columns
    df[string_columns] = df[string_columns].apply(lambda x: x.str.lower())
    return df

# Redefine the transform_data function using the specialized functions
def transform_data(df):
    """
    Apply transformations to the dataframe such as:
    - Standardizing date formats
    - Filling missing values
    - Converting text to lowercase
    """
    df = standardize_date_formats(df, ['Transaction_date', 'Account_Created', 'Last_Login'])
    df = fill_missing_values(df, {'State': 'Unknown', 'US Zip': 0})
    df = convert_text_to_lowercase(df)
    return df

df_transformed = transform_data(sales_data)
print(df_transformed.head())
output_file_path = '/Users/paramanandbhat/Downloads/transformed_sales_data.csv'

# Export the transformed DataFrame to a CSV file
df_transformed.to_csv(output_file_path, index=False)

# Displaying the path to the CSV file after saving
output_file_path