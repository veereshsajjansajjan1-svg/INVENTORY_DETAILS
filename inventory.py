import sys

if len(sys.argv) != 5:
    print("Arguments not provided correctly. Using User values...\n")

    product_name = sys.argv[1]
    quantity = int(sys.argv[2])
    brand = sys.argv[3]
    price = float(sys.argv[4])

else:

 default_product = "UnknownProduct"
 default_quantity = 0
 default_brand = "NoBrand"
 default_price = 0.0

print("\n -- Inventory Details --")
print(f"Product Name: {product_name}")
print(f"Quantity: {quantity}")
print(f"Brand: {brand}")
print(f"Price: ${price:.2f}")

