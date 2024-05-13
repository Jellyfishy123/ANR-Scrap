import requests
from bs4 import BeautifulSoup

# Initialize count
count = 0

# Iterate over pages
for page_num in range(25):  # 25 pages in total (pages are 0-indexed)
    # Construct URL for the current page
    url = f"https://www.anr-technologies.com/collections/all?page={page_num}&sort_by=title-ascending"

    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all product names
        product_names = soup.find_all("div", class_="grid-product__title")

        # Extract and print the product names
        for product in product_names:
            # Encode the product name using UTF-8 with error handling to ignore non-Unicode characters
            name = product.text.strip().encode("utf-8", errors="ignore")
            print(name)
            count += 1

        print(f"Number of items on page {page_num}: {len(product_names)}")
    else:
        print(f"Failed to retrieve webpage for page {page_num}")

print("Total number of items:", count)
