import scrapy
import pandas as pd


list_name = []
list_cat = []

class QuotesSpider(scrapy.Spider):
    name = "fakeplants"
    start_urls = ['https://www.fake-plants.co.uk/']

    # Follow links
    def parse(self, response):
        for item in response.css('li.product-category a::attr(href)'):
            yield response.follow(item.get(), callback=self.parse_categories)

    def parse_categories(self, response):
        products = response.css('div.astra-shop-summary-wrap')
        for product in products:
            name = product.css('h2.woocommerce-loop-product__title::text').get()
            Categories = product.css('span.ast-woo-product-category::text').get().strip()
            
            list_name.append(name)
            list_cat.append(Categories)

            # print(f'Nama : {list_name} and Categories : {list_cat}')
        df = pd.DataFrame({
            'Categories': list_cat,
            'Name': list_name
        })
        df.to_excel('datas.xlsx', index=False)
