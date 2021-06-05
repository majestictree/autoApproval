import time
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pyautogui as pg

# ログオンURL
url = 'https://docs.google.com/spreadsheets/d/15eEMGRNm3tkMwhpxdJRpdnfFU6BA5ajoyVlhUTaaYdM/edit?usp=sharing&userstoinvite=yuki.majestic.tree@gmail.com&ts=60b6fb2f'
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('--profile-directory=Profile 1')
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(10)
pg.click(x=928,y=644)
time.sleep(5)
driver.get(url)
time.sleep(10)
pg.click(x=928,y=644)
#driver.close()
#//*[@id="ritz-main-frame"]
# /html/body/iframe[4]
# /html/body/iframe[5]
# //*[@id=":un.contentEl"]/iframe
# /html/body/iframe[6]
# //*[@id="apiproxy8faca9d693d25487f6779b46d295e02c7e4a70b20.1963044138"]
# //*[@id="__HC_94253229"]/iframe
# //*[@id="apiproxy8faca9d693d25487f6779b46d295e02c7e4a70b20.1963044138"]
# //*[@id=":un.contentEl"]/iframe
#\:uh\.contentEl
