import mysql.connector as mysql
import pandas as pd

def load_data_to_db(df):
    """
    Load data into the MySQL database.

    :param df: DataFrame containing the transformed sales data.
    """
    # Database connection parameters
    db_params = {
    'host': 'localhost',
    'user': 'yourusername',
    'password': 'yourpassword',
    'database': 'sales_data'
}
    # Establish a database connection
    db_conn = mysql.connect(**db_params)
    cursor = db_conn.cursor()

    # Prepare the insert query
    insert_query = """
    INSERT INTO transactions (Transaction_date, Product, Price, Payment_Type, Name, City, State, Country, Account_Created, Last_Login, Latitude, Longitude, US_Zip)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Insert data into the database
    for index, row in df.iterrows():
        cursor.execute(insert_query, tuple(row))
        db_conn.commit()

    # Close the connection
    cursor.close()
    db_conn.close()

    print('Loading is successful')



# Load the transformed data into a DataFrame (assuming it's already transformed)
transformed_sales_data = pd.read_csv('/Users/paramanandbhat/Downloads/transformed_sales_data.csv')  

# Call the load function
load_data_to_db(transformed_sales_data)
