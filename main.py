from Product import Product

print("Sample url: https://mechanicalkeyboards.com/shop/index.php?l=product_detail&p=4322")
url = input("Enter the product url from the mechanicalkeyboards.com website:")
product = Product(url)

print("Your selected keyboard:")
print(product.get_json())