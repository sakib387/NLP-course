from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
from PIL import Image
from io import BytesIO

driver = webdriver.Chrome()

driver.get('https://www.daraz.com.bd/products/tws-rrrrr-i323422801-s1695718790.html?scm=1007.51610.379274.0&pvid=6eefc127-f526-41c0-816d-a992a1d48604&search=flashsale&spm=a2a0e.tm80335411.FlashSale.d_323422801')
time.sleep(3)  # Wait for page to load

text = driver.find_element(By.XPATH, '//*[@id="module_product_title_1"]/div/div/h1').text
link = driver.find_element(By.XPATH, '//*[@id="module_item_gallery_1"]/div/div[1]/div/img').get_attribute('src')
image = requests.get(link)

print("######")
print(link)
print(text)

# Save the image to a file
with open("downloaded_image.jpg", "wb") as f:
    f.write(image.content)
print("Image downloaded as downloaded_image.jpg")

# Optionally, you can still display it using PIL if you want
img = Image.open(BytesIO(image.content))
img.show()

driver.quit() # Close the browser when done