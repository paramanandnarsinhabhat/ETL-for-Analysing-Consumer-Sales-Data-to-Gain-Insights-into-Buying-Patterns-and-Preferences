import pandas as pd
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Now you can import common_utils
from utilities import common_utils

def extract(file_path):
    """
    Extract data from a CSV file using the common_utils read_csv_file function.
    
    :param file_path: Path to the CSV file to be read.
    :return: Pandas DataFrame containing the data from the CSV file.
    """
    return common_utils.read_csv_file(file_path)

# Define the path to the CSV file
csv_file_path = '/Users/paramanandbhat/Downloads/SalesJan2009.csv'

# Call the extract method to read the data
sales_data = extract(csv_file_path)

# Display the first few rows of the DataFrame
print(sales_data.head())
