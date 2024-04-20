# Amazon Price Tracker

This Python program tracks the price of a specific product on Amazon and sends an email notification if the price drops below a target price.

## Features

- Scrapes the Amazon product page to extract the product title and current price.
- Compares the price with a target price.
- Sends an email alert if the current price is lower than the target price.

## Prerequisites

Before running the program, make sure you have the following installed:

- Python 3.x
- `requests` library (`pip install requests`)
- `beautifulsoup4` library (`pip install beautifulsoup4`)
- `dotenv` library (`pip install python-dotenv`)

## Setup

1. Clone this repository to your local machine:
````
git clone https://github.com/your-username/amazon-price-tracker.git
````
2. Create a `.env` file in the project directory and add the following environment variables:

````
MY_EMAIL=your_email@gmail.com
MY_EMAIL_PASSWORD=your_email_password
TO_EMAIL=recipient_email@example.com
````

Replace `your_email@gmail.com` with your Gmail email address, `your_email_password` with your Gmail password, and `recipient_email@example.com` with the recipient's email address.

3. Modify the `TARGET_PRICE` and `URL` variables in the `main.py` file according to your requirements.


The program will scrape the Amazon product page, compare the price with the target price, and send an email alert if the price drops below the target.

## Note

- This program uses Gmail's SMTP server for sending email alerts. Make sure to enable less secure apps in your Gmail settings or use an app password if you have two-factor authentication enabled.
- Use this program responsibly and avoid making too many requests to Amazon's servers to prevent being blocked.


