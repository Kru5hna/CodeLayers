from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)


def scrape_amazon_product(url):
    driver.get(url)
    time.sleep(4)

    data = {
        "platform": "Amazon",
        "product_url": url
    }

    # Product name
    try:
        data["product_name"] = driver.find_element(By.ID, "productTitle").text.strip()
    except:
        data["product_name"] = None

    # Brand (best-effort)
    try:
        data["brand"] = driver.find_element(
            By.XPATH, "//tr[th[text()='Brand']]/td"
        ).text
    except:
        data["brand"] = data["product_name"].split()[0] if data["product_name"] else None

    # Price
    try:
        data["price"] = driver.find_element(
            By.CSS_SELECTOR, "span.a-price span.a-offscreen"
        ).text.replace("₹", "").replace(",", "")
    except:
        data["price"] = None

    # MRP
    try:
        data["mrp"] = driver.find_element(
            By.CSS_SELECTOR, "span.a-text-price span.a-offscreen"
        ).text.replace("₹", "").replace(",", "")
    except:
        data["mrp"] = None

    # Discount (derived)
    try:
        if data["price"] and data["mrp"]:
            data["discount_percent"] = round(
                (float(data["mrp"]) - float(data["price"])) / float(data["mrp"]) * 100, 2
            )
        else:
            data["discount_percent"] = None
    except:
        data["discount_percent"] = None

    # Product rating
    try:
        data["product_rating"] = driver.find_element(
            By.CSS_SELECTOR, "span.a-icon-alt"
        ).text
    except:
        data["product_rating"] = None

    # Number of ratings
    try:
        data["num_ratings"] = driver.find_element(
            By.ID, "acrCustomerReviewText"
        ).text
    except:
        data["num_ratings"] = None

    # Seller name
    try:
        data["seller_name"] = driver.find_element(
            By.ID, "sellerProfileTriggerId"
        ).text
    except:
        data["seller_name"] = "Amazon"

    try:
        data["review_text"] = driver.find_element(
            By.CSS_SELECTOR, "div[data-hook='review-collapsed'] span"
        ).text
        data["review_rating"] = driver.find_element(
            By.CSS_SELECTOR, "i[data-hook='review-star-rating'] span"
        ).text
    except:
        data["review_text"] = None
        data["review_rating"] = None

    return data
    driver.get(url)
    time.sleep(3)

    data = {}

    try:
        data["product_name"] = driver.find_element(By.ID, "productTitle").text.strip()
    except:
        data["product_name"] = None

    try:
        data["price"] = driver.find_element(By.CLASS_NAME, "a-price-whole").text.replace(",", "")
    except:
        data["price"] = None

    try:
        data["product_rating"] = driver.find_element(By.CLASS_NAME, "a-icon-alt").text
    except:
        data["product_rating"] = None

    try:
        data["num_ratings"] = driver.find_element(By.ID, "acrCustomerReviewText").text
    except:
        data["num_ratings"] = None

    try:
        data["seller_name"] = driver.find_element(By.ID, "sellerProfileTriggerId").text
    except:
        data["seller_name"] = "Amazon"

    data["platform"] = "Amazon"

    return dat
def scrape_flipkart_product(url):
    driver.get(url)
    time.sleep(4)

    data = {
        "platform": "Flipkart",
        "product_url": url
    }

    try:
        data["product_name"] = driver.find_element(By.CLASS_NAME, "B_NuCI").text
    except:
        data["product_name"] = None

    try:
        data["brand"] = data["product_name"].split()[0]
    except:
        data["brand"] = None

    try:
        data["price"] = driver.find_element(By.CLASS_NAME, "_30jeq3").text.replace("₹", "").replace(",", "")
    except:
        data["price"] = None

    try:
        data["mrp"] = driver.find_element(By.CLASS_NAME, "_3I9_wc").text.replace("₹", "").replace(",", "")
    except:
        data["mrp"] = None

    try:
        data["product_rating"] = driver.find_element(By.CLASS_NAME, "_3LWZlK").text
    except:
        data["product_rating"] = None

    try:
        data["num_ratings"] = driver.find_element(By.CLASS_NAME, "_2_R_DZ").text
    except:
        data["num_ratings"] = None

    return data

    driver.get(url)
    time.sleep(3)

    data = {}

    try:
        data["product_name"] = driver.find_element(By.CLASS_NAME, "B_NuCI").text
    except:
        data["product_name"] = None

    try:
        data["price"] = driver.find_element(By.CLASS_NAME, "_30jeq3").text.replace("₹", "").replace(",", "")
    except:
        data["price"] = None

    try:
        data["product_rating"] = driver.find_element(By.CLASS_NAME, "_3LWZlK").text
    except:
        data["product_rating"] = None

    try:
        data["num_ratings"] = driver.find_element(By.CLASS_NAME, "_2_R_DZ").text
    except:
        data["num_ratings"] = None

    data["platform"] = "Flipkart"
    return data


def scrape_meesho_product(url):
    driver.get(url)
    time.sleep(4)

    data = {
        "platform": "Meesho",
        "product_url": url
    }

    try:
        data["product_name"] = driver.find_element(By.TAG_NAME, "h1").text
    except:
        data["product_name"] = None

    try:
        data["price"] = driver.find_element(By.CSS_SELECTOR, "span[data-testid='product-price']").text.replace("₹", "")
    except:
        data["price"] = None

    try:
        data["brand"] = data["product_name"].split()[0]
    except:
        data["brand"] = None

    return data

    driver.get(url)
    time.sleep(3)

    data = {}

    try:
        data["product_name"] = driver.find_element(By.TAG_NAME, "h1").text
    except:
        data["product_name"] = None

    try:
        data["price"] = driver.find_element(By.CLASS_NAME, "Text__StyledText-sc-oo0kvp-0").text.replace("₹", "")
    except:
        data["price"] = None

    data["platform"] = "Meesho"
    return data

def get_amazon_product_urls(search_url, pages=1, limit_per_page=5):
    links = set()

    for page in range(1, pages + 1):
        driver.get(search_url + f"&page={page}")
        time.sleep(2)

        products = driver.find_elements(
            By.CSS_SELECTOR, "a.a-link-normal.s-no-outline"
        )

        for p in products:
            href = p.get_attribute("href")
            if href and "/dp/" in href:
                links.add(href.split("?")[0])
            if len(links) >= pages * limit_per_page:
                return list(links)

    return list(links)

    driver.get(search_url)
    time.sleep(4)

    links = set()
    products = driver.find_elements(By.CSS_SELECTOR, "a.a-link-normal.s-no-outline")

    for p in products:
        href = p.get_attribute("href")
        if href and "/dp/" in href:
            links.add(href.split("?")[0])
        if len(links) >= limit:
            break

    return list(links)


amazon_search_urls = [
    "https://www.amazon.in/s?k=iphone",
    "https://www.amazon.in/s?k=bluetooth+earphones",
    "https://www.amazon.in/s?k=nike+shoes",
    "https://www.amazon.in/s?k=smart+watch",
]

flipkart_search_urls = [
    "https://www.flipkart.com/search?q=iphone",
    "https://www.flipkart.com/search?q=bluetooth+earphones",
    "https://www.flipkart.com/search?q=power+bank",
    "https://www.flipkart.com/search?q=nike+shoes",
]

meesho_search_urls = [
    "https://www.meesho.com/search?q=earphones",
    "https://www.meesho.com/search?q=smart+watch",
    "https://www.meesho.com/search?q=shoes",
    "https://www.meesho.com/search?q=charger",
]

def get_flipkart_product_urls(search_url, pages=1, limit_per_page=5):
    links = set()

    for page in range(1, pages + 1):
        driver.get(search_url + f"&page={page}")
        time.sleep(2)

        products = driver.find_elements(By.CSS_SELECTOR, "a._1fQZEK")

        for p in products:
            href = p.get_attribute("href")
            if href:
                links.add("https://www.flipkart.com" + href)
            if len(links) >= pages * limit_per_page:
                return list(links)

    return list(links)

def get_meesho_product_urls(search_url, pages=1, limit_per_page=5):
    links = set()

    for page in range(1, pages + 1):
        driver.get(search_url + f"&page={page}")
        time.sleep(2)

        products = driver.find_elements(By.CSS_SELECTOR, "a[href*='/product/']")

        for p in products:
            href = p.get_attribute("href")
            if href:
                links.add(href)
            if len(links) >= pages * limit_per_page:
                return list(links)

    return list(links)

records = []

for search_url in amazon_search_urls:
    product_urls = get_amazon_product_urls(search_url, pages=2)

    for url in product_urls:
        try:
            print("Amazon:", url)
            records.append(scrape_amazon_product(url))
        except:
            pass


for search_url in flipkart_search_urls:
    product_urls = get_flipkart_product_urls(search_url, pages=2)

    for url in product_urls:
        try:
            print("Flipkart:", url)
            records.append(scrape_flipkart_product(url))
        except:
            pass

for search_url in meesho_search_urls:
    product_urls = get_meesho_product_urls(search_url, pages=2)

    for url in product_urls:
        try:
            print("Meesho:", url)
            records.append(scrape_meesho_product(url))
        except:
            pass

df = pd.DataFrame(records)
df.to_csv("ecommerce_grey_market_data.csv", index=False)
