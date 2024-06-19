# Web Scraper for E-commerce Product Data

## Description

This project is a web scraper designed to collect product data from e-commerce websites and store it in a MongoDB database. The scraper extracts details such as product title, price, rating, review count, and image URLs from specified product pages. The data is then organized and stored for easy access and further processing.

## Features

- **Scrapes Product Data**: Collects product details including title, price, rating, and review count from e-commerce websites.
- **Image URL Extraction**: Retrieves the image URL of each product and updates the database accordingly.
- **MongoDB Integration**: Stores the scraped data in a MongoDB database for efficient querying and data management.
- **Retry Mechanism**: Implements a retry mechanism to handle network issues and ensure data is correctly fetched.

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/web-scraper-ecommerce.git
    cd web-scraper-ecommerce
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up MongoDB**
    - Ensure MongoDB is installed and running on your local machine.
    - Create a database named `ecommerce`.

4. **Run the Scraper**
    ```bash
    python main.py
    ```

## Usage

- The scraper fetches data from a predefined list of product URLs.
- It extracts product details and stores them in a MongoDB collection named `products`.
- The script also updates product image URLs by scraping the respective product pages.

## Configuration

- Update the MongoDB connection string in the script if needed.
- Modify the list of product URLs to scrape data from different sources.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.



