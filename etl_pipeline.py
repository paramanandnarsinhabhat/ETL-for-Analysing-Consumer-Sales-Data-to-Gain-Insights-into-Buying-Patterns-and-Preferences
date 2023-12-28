import pandas as pd
import sys
import os


# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Now you can import common_utils
from utilities import common_utils
from data.data_extraction.extraction import extract
from data.data_transformation.transform import transform_data
from data.data_loading.load import load

csv_file_path = '/Users/paramanandbhat/Downloads/SalesJan2009.csv'

def run_etl():
    # Extract
    extracted_data = extract(csv_file_path)

# Transform
    transformed_data = transform_data(extracted_data)

    


run_etl()