import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import time

# MongoDB connection setup
client = MongoClient() # add your database here, ecommerce and prodcuts should be renamed to your relevant fields
db = client['ecommerce']
collection = db['products']

# Headers to mimic a real browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def get_product_data(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('span', {'id': 'productTitle'}).text.strip()
        price = soup.find('span', {'id': 'priceblock_ourprice'}).text.strip()
        rating = soup.find('span', {'id': 'acrPopover'})['title'].strip()
        review_count = soup.find('span', {'id': 'acrCustomerReviewText'}).text.strip()
        return {'title': title, 'price': price, 'rating': rating, 'review_count': review_count, 'url': url}
    else:
        return None

def get_image_url(url):
    for _ in range(3):  # Retry mechanism
        try:
            response = requests.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Try different ways to find the image element
                image_element = soup.find('img', {'id': 'landingImage'}) or \
                                soup.find('img', {'data-old-hires': True}) or \
                                soup.find('img', {'class': 'a-dynamic-image'})

                if image_element:
                    return image_element['src']
                else:
                    print(f"Image element not found for {url}")
            else:
                print(f"Request failed with status code {response.status_code} for {url}")
        except requests.exceptions.RequestException as e:
            print(f"Request exception {e} for {url}")
        time.sleep(1)  # Wait before retrying
    return None

# Example product URLs
product_urls = [
    'https://www.amazon.com/Apple-2024-MacBook-15-inch-Laptop/dp/B0CX23GFMJ',
    'https://www.amazon.com/Apple-2024-MacBook-13-inch-Laptop/dp/B0CX22ZW1T',
    'https://www.amazon.com/Apple-MacBook-Laptop-12-core/dp/B0CM5KXTND',
    'https://www.amazon.com/2022-Apple-MacBook-Laptop/dp/B0B3CDZLTB',
    'https://www.amazon.com/HP-Pavilion-Business-Touchscreen-Processor/dp/B0C91Q3YBL',
    'https://www.amazon.com/HP-Touchscreen-i7-13700H-Processor-Backlit/dp/B0CFCJXF4D',
    'https://www.amazon.com/HP-Pavilion-Business-Touchscreen-Processor/dp/B0C7JBSZ7G',
    'https://www.amazon.com/HP-Newest-ENVY-Laptop/dp/B0D64R2BSM',
    'https://www.amazon.com/HP-Laptop/dp/B0D5M5FSSV'
]

for url in product_urls:
    product_data = get_product_data(url)
    if product_data:
        image_url = get_image_url(url)
        if image_url:
            product_data['image'] = image_url
        collection.insert_one(product_data)
        print(f"Inserted data for {product_data['title']}")
    else:
        print(f"Failed to fetch data for {url}")

print("Data scraping and insertion completed.")
