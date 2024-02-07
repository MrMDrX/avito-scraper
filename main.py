import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def scrape_avito_page(url, headers):
    logging.info(f"Scraping page: {url}")
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        logging.info("Page retrieved successfully")
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup
    else:
        logging.error(f"Failed to retrieve page {url}. Status code: {response.status_code}")
        return None

def extract_listings(soup):
    listings = soup.find_all('a', class_='sc-1jge648-0 eTbzNs')
    data = []
    for listing in listings:
        seller = listing.find('p', class_='sc-1x0vz2r-0 dNKvDA').text
        location_div = listing.find('div', class_='sc-b57yxx-8 cnMHvz')
        location_full = location_div.find('p', class_='sc-1x0vz2r-0 iFQpLP').text.strip()
        location = location_full.split('dans')[-1].strip()
        title = listing.find('p', class_='sc-1x0vz2r-0 czqClV').text
        details = listing.find_all('span', class_='sc-1s278lr-0 cAiIZZ')
        car_details = [detail.text.strip() for detail in details]
        price_elem = listing.find('p', class_='sc-1x0vz2r-0 eCXWei sc-b57yxx-3 IneBF')
        price = price_elem.text.strip() if price_elem and price_elem.text.strip() != 'Prix non spécifié' else 'unspecified'
        image_url = listing.find('img', class_='sc-bsm2tm-3 dQOodK')['src']
        fuel_type = car_details[0] if car_details else 'unspecified'
        fiscal_power = car_details[1] if len(car_details) > 1 else 'unspecified'
        gearbox = car_details[2] if len(car_details) > 2 else 'unspecified'

        data.append({
            'Seller': seller,
            'Location': location,
            'Title': title,
            'Fuel Type': fuel_type,
            'Fiscal Power': fiscal_power,
            'Gearbox': gearbox,
            'Price': price,
            'Image URL': image_url
        })
    return data

def get_total_pages(url, headers):
    logging.info(f"Getting total pages from {url}")
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        pagination_div = soup.find('div', class_='sc-2y0ggl-0 hInuCx')
        last_page_link = pagination_div.find_all('a')[-2]
        total_pages = int(last_page_link.text)
        logging.info(f"Total Pages retrieved successfully: {total_pages} pages")
        return total_pages
    else:
        logging.error(f"Failed to retrieve page {url}. Status code: {response.status_code}")
        return None

def scrape_avito(url, headers=None, num_pages=None):
    total_pages = get_total_pages(url, headers)
    if total_pages and num_pages > total_pages:
        num_pages = total_pages
    
    data = []

    for page_num in range(1, num_pages + 1):
        page_url = f"{url}?o={page_num}" if page_num > 1 else url
        soup = scrape_avito_page(page_url, headers)
        if soup:
            page_data = extract_listings(soup)
            data.extend(page_data)

    df = pd.DataFrame(data)
    return df

def export_to_csv(data, filename):
    data.to_csv(filename+'.csv', index=False)
    logging.info(f"Data exported to {filename}.csv")

def main():
    url = input("Enter Avito URL: ")
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0',
               'Accept-Language': 'en-US,en;q=0.5',
               'Accept-Encoding': 'gzip, deflate, br'}
    num_pages = int(input("Enter the number of pages to scrape: "))
    filename = input("Enter the output filename (e.g., scraped_data.csv): ")

    scraped_data = scrape_avito(url, headers=headers, num_pages=num_pages)
    export_to_csv(scraped_data, filename)

if __name__ == "__main__":
    main()
