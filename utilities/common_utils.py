import pandas as pd

def read_csv_file(file_path):
    """
    Read a CSV file and return a DataFrame.

    :param file_path: Path to the CSV file
    :return: DataFrame containing the CSV data
    """
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error occurred while reading {file_path}: {e}")
        return None
