from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

from bs4 import BeautifulSoup

AUTH = 'brd-customer-hl_bf04910c-zone-datanaut_scrape:9lzozcx51sry'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'


def scrape_it(website):
    # Set up connection to remote Chrome via BrightData
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')

    # Set Chrome options if needed
    options = ChromeOptions()
    # options.add_argument('--headless')  # Optional: run headless

    with Remote(sbr_connection, options=options) as driver:
        print('Connected! Navigating...')
        driver.get(website)
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('page.png')
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html
    # This main code is provided form BrightData Docs for the connection of captcha overpaas tool provied by selenium python brightData


def main():
    url = 'https://example.com'
    html_content = scrape_it(url)
    print(html_content)
# the main function to scrape it usign url 

if __name__ == '__main__':
    main()



  # we dont want scripts and design and unecessary things from scraper to pass to out llm to get the data...


def extract_main_content(html_content):
     # Beautifulsoup is a html parser... we can collect html main data usign it
     soup = BeautifulSoup(html_content, "html.parser")
     body_cont = soup.body # main body elements parsing 
     if body_cont:
        return str(body_cont) # this statement basically says , if the body content exists then return th content in form of string else , we can simply reaturn and empty string
     return ""
     
def clean_the_body_content(body_cont):
    soup = BeautifulSoup(body_cont, "html.parser") # this will look inside the parsed content 

    for script_or_style in soup("script", "style"):
        script_or_style.extract() # every website has a scripts in js and style in css so we will iterate and remove them, and soup is defined as our beautifulsoup(body_content)

        cleaned_cont = soup.get_text(separator="/n") # this is getting all the text and seperating it with a new line 
        cleaned_cont = "/n".join(line.strip() for line in cleaned_cont.splitlines() if line.strip()) 
        # as soon as we grab content from html ,we will have our empty text strings , so , escentially we want to remove them so we are performing this method inside the .join function....

        # we are splitting the text in several batches , so that we can pass data to llm , as if there is too much descrete text and more than 8000 char , our llm cant take it all, so basically we are reducing the text in organised way , so that our llm can take data effeciently and later give us good responses 

        # out llm has token limit , so we are reducing text .... thats the trick 

        # considering that the token limit of llm is 8000 char , so we need less than it 

        # we will seperate data in multiple batches each having some chars ideally 6000 , and one by one passing them to the llm 

def split_dom_content(dom_content, max_length=6000):
      return[
        dom_content[i : i+max_length] for i in range(0,len(dom_content),max_length)]
            