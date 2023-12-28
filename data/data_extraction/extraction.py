import pandas as pd

def read_csv_file(file_path):
    """
    Read the CSV file into a pandas DataFrame.

    :param file_path: Path to the CSV file
    :return: Pandas DataFrame containing the CSV data
    """
    try:
        data = pd.read_csv(file_path)
        print("Data extracted successfully.")
        return data
    except Exception as e:
        print(f"Error occurred: {e}")

# Define the path to the CSV file
csv_file_path = '/Users/paramanandbhat/Downloads/SalesJan2009.csv' 

# Call the function to read the data
sales_data = read_csv_file(csv_file_path)
#  Display the first few rows of the DataFrame
print(sales_data.head())