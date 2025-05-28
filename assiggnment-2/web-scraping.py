#//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div/ul/li[8]/a
#//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div/ul/li[8]/a
#//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div/ul/li[8]/a
#//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div/ul/li[8]/a

#for number of pages in daraz i have found a pattern that, every last page has a common structure so we can easily find last page from this xpath

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
from PIL import Image
from io import BytesIO

driver = webdriver.Chrome()

driver.get('https://www.daraz.pk/toy-boxes/?up_id=463193942&clickTrackInfo=matchType--20___description--75%2525%2Boff___seedItemMatchType--c2i___bucket--0___spm_id--category.hp___seedItemScore--0.0___abId--379344___score--0.1___pvid--36fe1852-1f91-4927-a5ca-0a3161e47139___refer--___appId--7253___seedItemId--463193942___scm--1007.17253.379344.0___categoryId--10000761___timestamp--1748403512171&from=hp_categories&item_id=463193942&version=v2&q=toy%2Bboxes%2B%2Borganisers&params=%7B%22catIdLv1%22%3A%2210000336%22%2C%22pvid%22%3A%2236fe1852-1f91-4927-a5ca-0a3161e47139%22%2C%22src%22%3A%22ald%22%2C%22categoryName%22%3A%22Toy%2BBoxes%2B%2BOrganisers%22%2C%22categoryId%22%3A%2210000761%22%7D&src=hp_categories&spm=a2a0e.tm80335142.categoriesPC.d_7_10000761')
time.sleep(3)  # Wait for page to load

last_page = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div/ul/li[8]/a').text
print(last_page)

# here i have recived last page number

#now it't time to get all pages data
#//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/span
#//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[3]/span
#//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[40]/div/div/div[2]/div[3]/span
#//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/span

 
base_url = "https://www.daraz.pk/toy-boxes/?clickTrackInfo=matchType--20___description--75%2525%2Boff___seedItemMatchType--c2i___bucket--0___spm_id--category.hp___seedItemScore--0.0___abId--379344___score--0.1___pvid--36fe1852-1f91-4927-a5ca-0a3161e47139___refer--___appId--7253___seedItemId--463193942___scm--1007.17253.379344.0___categoryId--10000761___timestamp--1748403512171&from=hp_categories&item_id=463193942&version=v2&q=toy%2Bboxes%2B%2Borganisers&params=%7B%22catIdLv1%22%3A%2210000336%22%2C%22pvid%22%3A%2236fe1852-1f91-4927-a5ca-0a3161e47139%22%2C%22src%22%3A%22ald%22%2C%22categoryName%22%3A%22Toy%2BBoxes%2B%2BOrganisers%22%2C%22categoryId%22%3A%2210000761%22%7D&src=hp_categories&spm=a2a0e.tm80335142.categoriesPC.d_7_10000761"

 
driver.get(base_url)
time.sleep(3)

items_data = []

 
for page in range(1, int(last_page) + 1):
    print(f"Scraping page {page}...")
    url = base_url + f"&page={page}"
    driver.get(url)
    time.sleep(3)

   
    for i in range(1, 41):  # div[2] to div[40]
    
        try:
            xpath = f'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[3]/span'
            span = driver.find_element(By.XPATH, xpath)
            items_data.append(span.text)
        except:
            continue

print(f"\nTotal items collected: {len(items_data)}")

  