--Create a Database: Log into MySQL and create a new database for your project 
CREATE DATABASE sales_data;

--Create User and Grant Permissions (optional): For security, create a new user and grant it permissions to access and modify the new database.

CREATE USER 'yourusername'@'localhost' IDENTIFIED BY 'yourpassword';
GRANT ALL PRIVILEGES ON sales_data.* TO 'yourusername'@'localhost';
FLUSH PRIVILEGES;

--Design Table Schema: Determine the structure of your table(s) based on the transformed data. Create the necessary tables within the sales_data database.
USE sales_data;
CREATE TABLE transactions (
  id INT AUTO_INCREMENT PRIMARY KEY,
  Transaction_date DATETIME,
  Product VARCHAR(255),
  Price DECIMAL(10, 2),
  Payment_Type VARCHAR(50),
  Name VARCHAR(255),
  City VARCHAR(255),
  State VARCHAR(255),
  Country VARCHAR(255),
  Account_Created DATETIME,
  Last_Login DATETIME,
  Latitude DECIMAL(10, 8),
  Longitude DECIMAL(11, 8),
  US_Zip INT
);

