import csv
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

# Set up configurable parameters
num_customers = 1000
days_in_data = 180
base_date = datetime(2023, 1, 1)
seconds_day = 86400
status = {1:'open',2:'paid',3:'delivered'}
destination_path = 'mock_tpt_nos/mutables/'

# Generate mock customer data
customer_data = []
for customer_index in range(num_customers):
    customer_data.append([
        customer_index+1,
        fake.first_name(),
        fake.last_name(),
        fake.email()
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

for order_index in range(len(order_data)):
    for products_per_order in range(random.randint(1,20)):
        product_id = random.randint(1, 50)
        product_quantity = random.randint(1,5)
        order_product_data.append([
            f'{order_index+1}{products_per_order}',
            order_index+1,
            product_id,
            product_quantity 
        ])

# Write data to CSV files
with open(f'{destination_path}customers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "surname", "email"])
    writer.writerows(customer_data)

with open(f'{destination_path}orders.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["id", "customer_id", "order_status", "order_date"])
    writer.writerows(order_data)

with open(f'{destination_path}order_products.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["transaction_id","order_id", "product_id", "product_quantity"])
    writer.writerows(order_product_data)
