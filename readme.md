
# ETL Pipeline for Sales Data Analysis

## Overview
This project constructs an ETL (Extract, Transform, Load) pipeline in Python, designed to process and analyze sales data from January 2009. The pipeline streamlines the workflow of extracting data from a CSV file, cleansing and standardizing it through transformation, and finally loading the processed data into a SQLite database for comprehensive analysis.

## Technologies
- **Python**: The core language used for scripting the ETL process.
- **Pandas**: A powerful library for data manipulation and transformation.
- **SQL**: The language used for database interaction.

## Getting Started

### Prerequisites
- Ensure you have Python installed on your system.
- A virtual environment is recommended to manage dependencies.

### Installation
1. Clone the repository to your local machine:
   git clone https://github.com/paramanandnarsinhabhat/ETL-for-Analysing-Consumer-Sales-Data-to-Gain-Insights-into-Buying-Patterns-and-Preferences.git


2. Change directory to the project folder:
   cd ETL-for-Analysing-Consumer-Sales-Data-to-Gain-Insights-into-Buying-Patterns-and-Preferences


3. Install the required packages:
   pip install -r requirements.txt


### File Structure
- `requirements.txt`: This text file lists all the necessary Python libraries and dependencies required for the project.
- `data/SalesJan2009.csv`: Raw sales data file.
- `data_extraction/extraction.py`: Script for data extraction.
- `data_transformation/transform.py`: Script for data transformation.
- `data_loading/load.py`: Script for loading data into the database.
- `etl_pipeline.py`: Central script that orchestrates the ETL process.

## Usage
To run the ETL pipeline, execute the following command from the project root directory:
```bash
python etl_pipeline.py
```

### Scheduling
To schedule the ETL process, you can create a cron job:
1. Open your terminal and run `crontab -e` to edit your cron jobs.
2. Add the following line to schedule the pipeline to run daily at 3 AM:
   ```cron
   0 3 * * * /usr/bin/python /path/to/etl_pipeline.py
   ```
   Replace `/usr/bin/python` with the path to your Python executable and `/path/to/etl_pipeline.py` with the absolute path to the `etl_pipeline.py` file in your project directory.

## Optimization
- A module `utilities/common_utils.py` is implemented to centralize functions commonly used throughout the project, ensuring DRY principles and code reusability.

## MySQL Connector
To interact with the MySQL database, install the connector using pip:
```bash
pip install mysql-connector-python
```

## Notes
- Verify the path to `SalesJan2009.csv` in `extract.py`.
- Modify the cron job according to your requirements.
- The SQL script for creating the database schema is included within the project.
```

This `README.md` is organized  to provide a clear, professional, and logical flow of information. It includes sections on project overview, technology stack, setup instructions, file structure, usage guide, scheduling the ETL, optimization efforts, and additional notes for clarity and completeness.