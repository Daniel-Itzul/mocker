import csv
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

# Set up configurable parameters
num_customers = 1000
num_products = 50
days_in_data = 180
base_date = datetime(2023, 7, 1)
seconds_day = 86400
status = {1:'open',2:'paid',3:'delivered'}
destination_path = 'mock_mesh/events/'
source_path = 'mock_mesh/sources/'


# Generate mock customer data
# Not needed taken from original data.

# Generate mock stock data
# Read price data
product_prices = {}
with open(f'{source_path}source_products.csv', mode='r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Prices are already in cents, so directly store them as integers
        product_prices[int(row['product_id'])] = int(row['price_cents'])

stock_data = []
entry_id = 0
for day_correlative in range(days_in_data):
    entries_in_date = random.randint(0,2)
    for entry_correlative in range(entries_in_date):
        entry_id += 1
        product_id = random.randint(1, num_products)
        entry_date = base_date + timedelta(days=day_correlative)
        quantity = random.randint(1,20)
          # Get the selling price in cents from the dictionary
        selling_price_cents = product_prices.get(product_id, 0)  # Default to 0 if product_id not found
        # Fluctuate the purchase price around the selling price (in cents)
        fluctuation_percentage = random.uniform(-0.05, 0.05)  # Example fluctuation: -5% to +5%
        purchase_price_cents = int(selling_price_cents * (1 + fluctuation_percentage))
        stock_data.append([
            entry_id,
            product_id,
            quantity,
            purchase_price_cents,  # Add the purchase price in cents to the entry
            entry_date.strftime('%Y-%m-%d'),
        ])
    


# Generate mock order data
order_data = []
order_product_data = []
order_id = 1
for day_correlative in range(days_in_data):
    orders_in_date = random.randint(0,50)
    for order_correlative in range(orders_in_date):
        customer_id = random.randint(1, num_customers)
        order_date = base_date + timedelta(days=day_correlative)
        order_status = status[random.randint(1,3)]
        order_data.append([
            order_id + order_correlative,
            customer_id,
            order_status,
            order_date.strftime('%Y-%m-%d'),
        ])
    order_id += orders_in_date

#Generate Order_Product data, all orders have at least one product.

for order_index in range(1,len(order_data)+1):
    for products_per_order in range(random.randint(1,20)):
        product_id = random.randint(1, 50)
        product_quantity = random.randint(1,5)
        order_product_data.append([
            f'{order_index}{products_per_order}',
            order_index,
            product_id,
            product_quantity 
        ])

# Write data to CSV files

with open(f'{destination_path}source_orders.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["order_id", "customer_id", "order_status", "order_date"])
    writer.writerows(order_data)

with open(f'{destination_path}source_order_products.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["transaction_id","order_id", "product_id", "product_quantity"])
    writer.writerows(order_product_data)

with open(f'{destination_path}source_stock.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["entry_id","product_id", "product_quantity", "purchase_price_cents", "entry_date" ])
    writer.writerows(stock_data)

