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
product_id = 1
for day_correlative in range(days_in_data):
    entries_in_date = 3
    for entry_correlative in range(entries_in_date):
        entry_id += 1
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
        product_id += 1
    
with open(f'{destination_path}source_stock.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["entry_id","product_id", "product_quantity", "purchase_price_cents", "entry_date" ])
    writer.writerows(stock_data)

