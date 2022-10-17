from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://paytm.com/flights')
driver.maximize_window()

home_=driver.find_element('id','text-box')
home_.click()
home_.send_keys('pnq')
time.sleep(2)

city_list=driver.find_elements(By.XPATH,'//div[@class="_2xgL"]')



for city in city_list:
    new_city=city.text.split()
    if new_city[-1]=='PNQ':
        city.click()
        break

time.sleep(3)


#destination


destination_input=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[4]/div[1]/div[1]/input')
destination_input.click()
destination_input.send_keys('pat')
time.sleep(2)

city_list=driver.find_elements(By.CLASS_NAME,'_2xgL')



for city in city_list:
    new_city=city.text.split()
    if new_city[-1]=='PAT':
        city.click()
        break

#departure date
ddate=driver.find_element(By.XPATH,'//*[@id="datePickerOnward"]/div/div/input')
ddate.click()
destination_date=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[5]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[2]/div/div')
destination_date.click()
time.sleep(5)

#button click
button_click=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[8]/div/button')
button_click.click()
time.sleep(5)

#non-stop flight only
non_stop=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div/div[1]/div[3]/div/div/div[1]/div')
non_stop.click()
time.sleep(1)

#book_button

book_button=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[3]/div[1]/div[9]/a')
book_button.click()
time.sleep(3)

#switch_to_child window
child_window=driver.window_handles[1]
driver.switch_to.window(child_window)
time.sleep(5)

#continue button click
button3=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[2]/div/div[3]/button')

button3.click()
time.sleep(9)

#now it will ask login to continue after you have to login and do it manually








    




