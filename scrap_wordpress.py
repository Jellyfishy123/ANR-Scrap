import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://anrtechnologies.org/category-product/electrochemical-setups/?sss="
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all product names
    product_names = soup.find_all("h3", class_="product-title")

    # Extract and print the product names
    for product in product_names:
        print(product.text.strip())
else:
    print("Failed to retrieve the webpage.")
