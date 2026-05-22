import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime

# 1. Target URL (Supplier Website)
url = "http://books.toscrape.com/"
print("Website-kku connect pandrom...")

# 2. Internet-kulla poyi page-a fetch pandrom
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products_data = []

# 3. Page-la irukka ella products-aiyum thedurom
# HTML tags-a use panni exact data-va edukurom
items = soup.find_all('article', class_='product_pod')

print(f"Kandupudicha products count: {len(items)}\n")

for item in items:
    # Product peru
    name = item.h3.a['title']
    # Vilai (Price) - Idhula thevaiyillatha special characters irukkum (namma transform phase-la clean pannuvom)
    price = item.find('p', class_='price_color').text
    # Stock irukka illaya?
    stock = item.find('p', class_='instock availability').text.strip()
    # Innaiku date
    today_date = datetime.now().strftime("%d-%m-%Y")

    # Data-va oru dictionary-la podrom
    products_data.append({
        'product_name': name,
        'supplier_price': price,
        'stock_status': stock,
        'record_date': today_date
    })

# 4. DataFrame-a maathi raw_data folder-la save pandrom
df = pd.DataFrame(products_data)

# --- INTHA PUDHU CODE-A ADD PANNUNGA ---
# raw_data folder illana, athuve create pannidum (The Pro Data Engineer Touch)
output_dir = 'raw_data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"'{output_dir}' folder illai, so puthusa create pannittan!")
# --------------------------------------

# File name-la innaiku date-a attach pandrom (Daily pipeline madhiri)
file_name = f"{output_dir}/live_supplier_data_{datetime.now().strftime('%Y%m%d')}.csv"

df.to_csv(file_name, index=False)
print(f"Success Boss! Live data theliva scrape aagi '{file_name}'-la save aagiduchu 🚀")