import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pyautogui as pg

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('--profile-directory=Profile 1')
driver = webdriver.Chrome(options=options)
 
def approve(url):
   driver.get(url)
   time.sleep(7)
   pg.click(x=928,y=644)
   time.sleep(5)

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
c = ServiceAccountCredentials.from_json_keyfile_name('approve-315805-9a0b1d8f202a.json', scope)

gs = gspread.authorize(c)

SPREADSHEET_KEY = '1q_tIweaYsO92VsdeB7VLlIF6RicV-66O6fV0HoJiKZ4'
workbook = gs.open_by_key(SPREADSHEET_KEY)
worksheet = workbook.worksheet('sheet1')
values = worksheet.get_all_values()
#workbook.del_worksheet(worksheet)
#workbook.add_worksheet(title='sheet1', rows=1000, cols=10)
for i in range(0, len(values)):
    print(values[i][0])
    if ((values[i][0][:3] == 'yuk') and (values[i][0][-9:] == 'gmail.com')):
        approve(values[i][1]);


