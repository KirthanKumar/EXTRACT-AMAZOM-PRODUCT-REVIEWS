# Python project for extracting amazon reviews using requests, beautiful soup and soax
import requests
import pandas  as pd
from bs4 import BeautifulSoup
import random
# go to soax.com and register

# while(True):
#     proxy = {
#         "http": f"http://Kh072ICB0vRFuRg9:wifi;;@proxy.soax.com:{9000+random.randint(0, 9)}",
#         "https": f"https://Kh072ICB0vRFuRg9:wifi;;@proxy.soax.com:{9000+random.randint(0, 9)}"
#     }

#     response = requests.get("http://checker.soax.com/api/ipinfo", proxies=proxy)
#     print(response.text)

def extractReviews(allReviews):
    resp = requests.get(allReviews)
    soup = BeautifulSoup(resp.text, 'html.parser')
    reviews = soup.findAll('div', {'data-hook':'review'})
    # print(reviews)
    count = 0
    for item in reviews:
        # with open('outputs/index2.html', 'w') as f:
        #     f.write(str(item))
        # print(item)
        # break
        review = {
            'ProductTitle': soup.title.text.replace("Amazon.in:Customer reviews:", "").strip(),
            'Review Title':item.find('span', {'class':'a-size-base'}).text.strip(),
            'Rating': item.find('span', {'class':'a-icon-alt'}).text.strip(),
            'Review Body': item.find('span', {'data-hook': 'review-body'}).text.strip()
        }
        count = count +1
        print("REVIEW NUMBER : " + str(count))
        print(review)
        
    
def main():
    productURL = "https://www.amazon.in/HP-i5-11400H-graphics-response-16-d0310TX/dp/B0BSFZ3ZS6/ref=cm_cr_arp_d_product_top?ie=UTF8"
    
    reviewURL = productURL.replace("dp", "product-reviews")
    # https://www.amazon.in/HP-i5-11400H-graphics-response-16-d0310TX/product-reviews/B0BSFZ3ZS6/ref=cm_cr_arp_d_product_top?ie=UTF8
    
    allReviews = reviewURL+"&reviewerType=all_reviews"
    # https://www.amazon.in/HP-i5-11400H-graphics-response-16-d0310TX/product-reviews/B0BSFZ3ZS6/ref=cm_cr_arp_d_product_top?ie=UTF8&reviewerType=all_reviews
    
    extractReviews(allReviews)

main()
