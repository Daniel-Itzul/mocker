import csv
import random

# Set up configurable parameters
num_order_products = 50000
assumed_number_orders = 5000
min_products_order = 2
max_products_order = 20
destination_path = 'grocery_list/mutables/'

# Generate mock order product data
order_product_data = []

#Generate Order_Product data, all orders have at least one product.

for i in range(assumed_number_orders):
    for j in range(random.randint(1,max_products_order+1)):
        order_id = i+1
        product_id = random.randint(1, 200)
        add_cart_order = j+1
        order_product_data.append([
            order_id,
            product_id,
            add_cart_order
        ])

# Write data to CSV files
with open(f'{destination_path}order_products.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["order_id", "product_id", "add_cart_order"])
    writer.writerows(order_product_data)
