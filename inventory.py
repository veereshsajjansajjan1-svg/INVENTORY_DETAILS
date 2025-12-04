import sys

if len(sys.argv) != 5:
    print("Usage: python inventory.py <product_name> <quantity> <brand> <price>")   
    sys.exit()

product_name = sys.argv[1]
quantity = int(sys.argv[2])
brand = sys.argv[3]
price = float(sys.argv[4])

print("\n -- Inventory Details --")
print(f"Product Name: {product_name}")
print(f"Quantity: {quantity}")
print(f"Brand: {brand}")
print(f"Price: ${price:.2f}")

if quantity > 50:
    print("Stock Status: High stock available")
else:
    print("Stock Status: Low stock available")
