import pandas as pd

# Replace 'file_path.parquet' with the actual path to your Parquet file
file_path = 'merged_data.parquet'

# Read the Parquet file into a pandas DataFrame
df = pd.read_parquet(file_path)

# Print the first few rows of the DataFrame
print(df.head(5))

# Print the total number of rows in the DataFrame
print("Total number of rows:", len(df))