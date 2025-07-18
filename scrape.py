# here we will use selenium 

# we will here write a function in python that just returns all of the content from that website 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time 


def scrape_it(website):
  print("Launching chrome browser.....")
  Chrome_Driver_Path = "chromedriver.exe"
  options = webdriver.ChromeOptions()
  driver = webdriver.Chrome(service=Service(Chrome_Driver_Path), options = options)

  try:
    driver.get(website)
    print("Page loaded...")
    html = driver.page_source# this is how we grapt html content of the page
    time.sleep(7) # this 7 seconds specifies for how long that particular website wil open and the nclose after retrieving data 
    return html 
  finally:
    driver.quit()