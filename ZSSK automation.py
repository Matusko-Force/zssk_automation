from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options #Setting up special options in order to not quit automatically
from selenium.webdriver.common.by import By #Importing by in order to work in brackets
import time #Importing time for pause
chrome_options = Options() #special options
chrome_options.add_experimental_option("detach", True) #special options

driver = webdriver.Chrome(options=chrome_options)






driver.get('https://predaj.zssk.sk/search') #Opening zssk page
time.sleep(2)
COOKIESbutton = driver.find_element(By.ID,"c-p-bn").click()# clicking cookies button
time.sleep(2)

Searchloginname = driver.find_element(By.ID, "fromInput") #Finding element for boarding station
Searchloginname.send_keys("Košice") # inputing boarding station
time.sleep(2)
Searchloginpassword = driver.find_element(By.ID, "toInput")# Finding element for arriving station
Searchloginpassword.send_keys("Bratislava hl.st.")# inputing ariving station

time.sleep(2)
obedbutton = driver.find_element(By.ID,"departDate").click() #clicking on calendar 
time.sleep(2)

time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[3]/div/div/form/div[1]/div/div[2]/span/div/div[1]/table/tbody/tr[3]/td[6]/div").click() #finding the date elemnt and lciking
time.sleep(2)
Searchtimename = driver.find_element(By.ID, "departTime").click()# this needds to be clicked two times because of some bug
Searchtimename = driver.find_element(By.ID, "departTime").click()# this needds to be clicked two times because of some bug
Searchtimename = driver.find_element(By.ID, "departTime").clear()#clearing the set time


driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[3]/div/div/form/div[1]/div/div[2]/div[2]/div/input").send_keys("13:00") #Inputing time before the train leaves so the train you go on is first in the list

driver.find_element(By.ID,"actionSearchConnectionButton").click()#cliking search
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[3]/div/span/div/form/div/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/table").click()#cliking on the first train/ the one you go with
time.sleep(3)
driver.find_element(By.ID,"dayGroupLoop:0:eSalesConnectionLoop:0:j_idt357").click()# cliking on it again
time.sleep(3)
driver.find_element(By.ID,"actionIndividualContinue").click()# cliking continue
time.sleep(3)
driver.find_element(By.ID,"sidebar:sidebarForm:j_idt813").click()# cliking continue
time.sleep(3)
driver.find_element(By.ID,"wagonThumb-0-0-8").click()# cliking on the wagon you want
time.sleep(3)

element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[3]/div[3]/div[1]/form[1]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div[6]/div/div/svg/svg[44]/metadata/place") #sleecting seat 
time.sleep(3)
ActionChains(driver).move_to_element(element).click().perform()
time.sleep(3)
driver.find_element(By.ID,"ticketsForm:j_idt293:j_idt295").click()
