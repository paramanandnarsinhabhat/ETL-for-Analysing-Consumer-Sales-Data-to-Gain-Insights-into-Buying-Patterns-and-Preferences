import mysql.connector as mysql
import pandas as pd

# Load the transformed data into a DataFrame (assuming it's already transformed)
transformed_sales_data = pd.read_csv('/Users/paramanandbhat/Downloads/transformed_sales_data.csv')  

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


# Insert data into the database
for index, row in transformed_sales_data.iterrows():
    insert_query = """
    INSERT INTO transactions (Transaction_date, Product, Price, Payment_Type, Name, City, State, Country, Account_Created, Last_Login, Latitude, Longitude, US_Zip)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, tuple(row))
    db_conn.commit()

# Close the connection
cursor.close()
db_conn.close()

print('Loading is successful')