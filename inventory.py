import sys

if len(sys.argv) !=5:

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
        print("stock status: high stock available")
    else :
        print("stock status: low stock available")

        
