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
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6",
        "Priority": "u=0, i",
        # "Host": "httpbin.org",
        "Sec-Ch-Ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"macOS\"",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
}

amazon_product_page = requests.get(URL, headers=headers).text
# generate amazon.html for troubleshooeting
# with open('amazon.html', mode="w", encoding="utf-8") as fp:
#     fp.write(amazon_product_page)
soup = BeautifulSoup(amazon_product_page, "lxml")

string_price = soup.find(name='span', attrs={"class": "priceToPay"}).getText()
# remove first white space and the $ sign from the string
price = float(string_price[2:])
product_title = soup.select_one("span[id=productTitle]").getText().strip()
# print(price)
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
