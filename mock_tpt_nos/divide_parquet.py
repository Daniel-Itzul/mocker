import pandas as pd
import os

def split_parquet_to_csv(parquet_file, output_dir, n_splits):
    df = pd.read_parquet(parquet_file)

    # Calculate the size of each split
    split_size = len(df) // n_splits

    for i in range(n_splits):
        # Calculate start and end indices
        start = i * split_size
        end = (i + 1) * split_size if i < n_splits - 1 else len(df)
        
        # Split the DataFrame
        split_df = df.iloc[start:end]
        
        # Prepare output file path
        output_file = os.path.join(output_dir, f'split_{i+1}.csv')
        
        # Write to CSV
        split_df.to_csv(output_file, index=False)

        print(f"Data split {i+1} written to {output_file}")

# Usage
split_parquet_to_csv('merged_data.parquet', './mutables', n_splits=4)
