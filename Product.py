from bs4 import BeautifulSoup
import requests
import json


class _Behavior():
    def get_name(self):
        return self.product_detail_soup.find("h4", class_="name").text
    
    def get_sku(self):
        return self.product_detail_soup.find('div',class_="product-id").find("span",class_='id').text
    
    def get_img_url(self):
        return self.img_url_base + self.product_detail_soup.find('div',attrs={"style":'text-align: center;'}).find('a')['href']
    
    def get_switch_table(self):
        switch_price_dict = {
        "switch":{}
        }
        
        switch_table = self.product_detail_soup.find('table', class_='edition_switch_list')
        switch_type = switch_table.select("td.switch a")
        switch_price= switch_table.find_all("td", class_='price')
        
        
        for i in range(len(switch_type)):
            # if(type(switch_type[i].find('div')) != None):
            #     switch_type[i].find('div').decompose() 
            switch_price_dict['switch'].update({switch_type[i].text : switch_price[i].text })
        
        return switch_price_dict
    
    
    def get_product_spec(self):
        spec_table = self.product_detail_soup.find('table', class_='v3_specs')
        spec_table_field = spec_table.find_all("td", class_='field')
        spec_table_value= spec_table.find_all("td", class_='value')
        
        product_spec = {
        "spec": {}
        }

        
        for i in range(len(spec_table)): 
            product_spec['spec'].update({spec_table_field[i].text : spec_table_value[i].text})
            
        return product_spec
    
    def get_detail(self):
        name = self.get_name()
        sku = self.get_sku()
        img_url = self.get_img_url()
        switch_table = self.get_switch_table()
        spec_table = self.get_product_spec()
        
        self.product['sku']=sku
        self.product['name']=name
        self.product['img_url']=img_url
        self.product.update(switch_table)
        self.product.update(spec_table)
        
        return self.product
    
    def get_json(self):
        return json.dumps(self.get_detail(), indent=4)

class Product(_Behavior):
    img_url_base = "https://mechanicalkeyboards.com/shop/"
    
    
    def __init__(self,url) -> None:
        self.url = url
        self.product = {}
        self.product_detail_soup = BeautifulSoup(requests.get(url).text, 'html.parser')