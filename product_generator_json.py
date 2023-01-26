from Product import Product
import pandas as pd
import json
from os import path
import time

df = pd.read_csv("items.csv")
url_list = df['url'].to_list()

filename = 'products.json'

if ~path.exists(filename) :
        with open(filename,'w') as f:
            f.write("[]") 
            
for url in url_list:
    product = Product(url)
    prod_list = []

    with open(filename) as f:
        prod_list = json.load(f)

    prod_list.append(product.get_detail())

    with open(filename, 'w') as json_file:
        json.dump(prod_list, json_file, 
                            indent=4,  
                            separators=(',',': '))
        
    
    
    

