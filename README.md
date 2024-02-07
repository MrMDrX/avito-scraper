# Avito Scraper

Avito Scraper is a Python tool for scraping listings data from Avito, a popular online marketplace. It allows users to extract information about cars, apartments, houses, and villas for sale in Morocco.

## Features

- [x] Scrapes car listings data from Avito website.
- [x] Supports specifying the number of pages to scrape.
- [x] Provides customizable output filename for storing scraped data.
- [x] Handles pagination automatically to scrape multiple pages.

- [ ] Add ability to scrape more details in each item details page.
- [ ] Implement scraping functionality for apartments, houses, and villas.
- [ ] Enhance error handling and logging for better user feedback.
- [ ] Improve configuration options for customization.

## Tools Used

- Python
- BeautifulSoup: Python library for web scraping
- requests: Python library for making HTTP requests
- pandas: Python library for data manipulation and analysis

## Quick Start

1. Clone the repository:

   ```bash
   git clone https://github.com/MrMDrX/avito-scraper.git
   ```

2. Navigate to the Project Directory:

   ```bash
   cd avito-scraper
   ```

3. Create and Activate a Virtual Environment (Optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the script:

   ```bash
   python main.py
   ```

## Usage

Run the `main.py` script and follow the prompts to specify the Avito URL, the number of pages to scrape, and the output filename. The scraped data will be exported to a CSV file.

```bash
python main.py
```

## Contributing

Contributions are welcome! Please submit bug reports, feature requests, or pull requests to help improve this tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
