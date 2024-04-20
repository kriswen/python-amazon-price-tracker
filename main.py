import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
TARGET_PRICE = 100

load_dotenv()
email_host = "smtp.gmail.com"
port = 587
email_sender = os.environ.get("MY_EMAIL")
email_password = os.environ.get("MY_EMAIL_PASSWORD")
email_receiver = os.environ.get("TO_EMAIL")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
amazon_product_page = requests.get(URL, headers).text
soup = BeautifulSoup(amazon_product_page, "lxml")

price_whole = int(soup.find(class_="a-price-whole").getText().split(".")[0])
price_decimal = int(soup.select_one("span.a-price-fraction").getText())
price = price_whole + (price_decimal * 0.01)
product_title = soup.select_one("span[id=productTitle]").getText().strip()
# print(f"{product_title}\n${price}")

message = (f"Subject:Amazon Deal Alert\n\n"
           f"price for {product_title} is currently ${price}\n"
           f"Link to product page: {URL}".encode("utf-8"))

if price < TARGET_PRICE:
    # send email alert
    with smtplib.SMTP(email_host, port) as conn:
        conn.starttls()
        conn.login(user=email_sender, password=email_password)
        conn.sendmail(from_addr=email_sender, to_addrs=email_receiver, msg=message)
        print("email sent")
