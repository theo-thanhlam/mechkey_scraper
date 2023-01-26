from Product import Product

p = Product("https://mechanicalkeyboards.com/shop/index.php?l=product_detail&p=9247")

print(p.get_switch_table())