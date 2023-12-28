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

