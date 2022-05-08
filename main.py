from bs4 import BeautifulSoup
import requests
import smtplib as em
import lxml
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/conno/PycharmProjects/.env.txt")


my_email = os.getenv("email_")
password = os.getenv("email_pass_")

product_url = "https://www.amazon.com/Ninja-AF101-Fryer-Black-gray/dp/B07FDJMC9Q/ref=zg_bs_home-garden_25/140-4253211-0907126?pd_rd_i=B07FDJMC9Q&psc=1"
price_target = 90.00
headers = {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}


response = requests.get(product_url, headers=headers)

amazon_page = response.text
soup = BeautifulSoup(amazon_page, "lxml")
price = soup.find("span", class_="a-offscreen").getText()
product_title = soup.find("span", id="productTitle").getText().strip()
price_without_currency = float(price.split("$")[1])
price_as_float = float(price_without_currency)


if price_target >= price_as_float:

   with em.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="c896asda@aol.com",
                            msg=f"Subject: {product_title} price below target\n\n {product_title} is now less than your target at {price}"
                                f"\n\n Buy Here: {product_url}"
        )
