import csv
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

# Set up configurable parameters
days_in_data = 180
base_date = datetime(2023, 1, 1)
seconds_day = 86400
num_customers = 1000
p_methods = {1:'cash',2:'credit_card'}
destination_path = 'mock_tpt_nos/mutables/'

# Generate mock order data
visit_data = []
visit_product_data = []
visit_id = 1
for day_correlative in range(days_in_data):
    visits_in_date = random.randint(0,50)
    for visit_correlative in range(visits_in_date):
        customer_id = random.randint(1, num_customers)
        visit_duration_min = random.randint(1,60)
        visit_date = base_date + timedelta(days=day_correlative)
        payment_method = p_methods[random.randint(1,2)]
        visit_data.append([
            visit_id + visit_correlative,
            customer_id,
            visit_duration_min,
            payment_method,
            visit_date.strftime('%Y-%m-%d')
        ])
    visit_id += visits_in_date

#Generate Order_Product data, all orders have at least one product.

for visit_index in range(len(visit_data)):
    for products_per_order in range(random.randint(1,10)):
        product_id = random.randint(1, 50)
        product_quantity = random.randint(1,5)
        visit_product_data.append([
            visit_index + 1,
            product_id,
            product_quantity 
        ])

# Write data to CSV files

with open(f'{destination_path}visits.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["visit_id", "customer_id", "visit_duration", "payment_method", "order_date"])
    writer.writerows(visit_data)

with open(f'{destination_path}visit_products.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["visit_id", "product_id", "product_quantity"])
    writer.writerows(visit_product_data)
