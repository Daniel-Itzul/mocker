import pandas as pd

# Load data from CSV files into pandas DataFrames, specifying the data types for 'id' columns as int64
order_products_df = pd.read_csv('mutables/order_products.csv')
orders_df = pd.read_csv('./mutables/orders.csv')
customers_df = pd.read_csv('./mutables/customers.csv')
products_df = pd.read_csv('./constants/products.csv')


products_df.drop(columns=['category_name'], inplace=True)

# Merge order_products with orders on 'order_id' and 'id' columns respectively

merged_df = pd.merge(order_products_df, orders_df, left_on='order_id', right_on='id', suffixes=('_product', '_order'))

# Merge merged_df with customers on 'customer_id' and 'id' columns respectively
merged_df = pd.merge(merged_df, customers_df, left_on='customer_id', right_on='id', suffixes=('_order', '_customer'))

# Merge merged_df with products on 'product_id' and 'product_id' columns respectively
merged_df = pd.merge(merged_df, products_df, left_on='product_id', right_on='product_id', suffixes=('_customer', '_product'))

# Drop redundant columns after the merge
merged_df.drop(columns=['id_order', 'id_customer'], inplace=True)

# Save the merged DataFrame to a Parquet file

merged_df.to_parquet('merged_data.parquet', index=False)
