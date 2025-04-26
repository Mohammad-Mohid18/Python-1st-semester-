# Avialable stock there and there pricing:

stocks = {
    'apple':[50.5,300],
    'banana':[30.0,250],
    'peach':[80.5,150],
    'mango':[100.0,300]
}

def update_quantity(product_name,increased_quantity):
    if product_name in stocks:
        for details in stocks.values():
            price,quantity = details
        quantity += increased_quantity
        print(f'Updated quantity for {product_name}: {quantity}')
        if quantity == 0:
            del stocks[product_name]
            print(f'Product {product_name} removed from stocks as its finished')
            for products,info in stocks.items():
                print(f'{products,info}.')
    else:
        print(f'Product {product_name} not found in stocks.')

def available_products():
    total_price = 0
    print('available products:')
    for products,details in stocks.items():
        price,quantity = details
        total_price += price * quantity
        print(f'products available:{products}, there quantities are:{quantity}kgs and there total is:{total_price}$')

def get_product(product_name):
    total_price = 0
    if product_name in stocks:
        for details in stocks.values():
            price,quantity = details
            total_price += price * quantity
        print(f'Price for {product_name}: {price}$, available quantity: {quantity} kgs and its total price: {total_price}$')
    else:
        print(f'Product {product_name} not found in stocks.')

def add_product(product_name,price, quantity):
    if product_name in stocks:
        print(f'the product {product_name} already exists')
    else:
        stocks[product_name] = [price, quantity]
        print(f'Product {product_name} added successfully with initial quantity of {quantity} kgs and its price is: {price} $')
