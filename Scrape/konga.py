from playwright.sync_api import sync_playwright
import pandas as pd

def scrape_led_tvs(headless,url):
    all_products = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for x in range(1,8):
            page.goto(f"{url}?page={x}", wait_until="domcontentloaded")
            page.wait_for_selector("article")
            articles = page.locator("article").all()

            for article in articles:
                the_title = article.locator('h3').first
                title = the_title.inner_text() if the_title.count() > 0 else "N/A"
                the_price = article.locator('div.shared_priceBox__VaVU0 span').first
                price = the_price.inner_text() if the_price.count() > 0 else "N/A"
                the_seller = article.locator('form span.ListingCard_soldBy__shCRn').first
                seller = the_seller.inner_text() if the_seller.count() > 0 else "N/A"
                the_review = article.locator('form span.starRating_reviewText__fVgH2').first
                review = the_review.inner_text() if the_review.count() > 0 else "N/A"


                base_url = "https://www.konga.com"
                the_product_link = article.locator('div.ListingCard_listingCardMetaContainer__HCXHt a').nth(1)
                if the_product_link.count() > 0:
                    product_link_ = the_product_link.get_attribute('href')
                    product_link = base_url + product_link_ if product_link_ else "N/A"
                else:
                    product_link = "N/A"

                all_products.append({
                    "Title": title,
                    "Price": price,
                    "Seller": seller,
                    "Review": review,
                    "Product Link": product_link
                    })
                
        browser.close()
    return all_products

products = scrape_led_tvs(headless=True, url="https://www.konga.com/category/led-tvs-7776")

print(f"Scraped {len(products)} products")

df = pd.DataFrame(products)
print(df)
# df.to_csv("Led_TVs.csv",index=False)