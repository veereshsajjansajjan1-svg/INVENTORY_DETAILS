import sys

default_product = "UnknownProduct"
default_quantity = 0
default_brand = "NoBrand"
default_price = 0.0


if len(sys.argv) != 5:
    print("Arguments not provided correctly. Using default values...\n")
    
    product_name = default_product
    quantity = default_quantity
    brand = default_brand
    price = default_price

else:
    product_name = sys.argv[1]
    quantity = int(sys.argv[2])
    brand = sys.argv[3]
    price = float(sys.argv[4])

print("\n -- Inventory Details --")
print(f"Product Name: {product_name}")
print(f"Quantity: {quantity}")
print(f"Brand: {brand}")
print(f"Price: ${price:.2f}")

