import time

from selenium import webdriver
import pyperclip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import random
from selenium.webdriver import ActionChains

PATH = "C:\SeleniumWebDrivers\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
action = ActionChains(driver)
ARR1=[' ','hsepnmg622@xtryb.com','mdqxr64263@noqulewa.com','glfavda990@noquviti.com','cqsdbvv922@noquviti.com','jpszxp7713@nowlike.com','zuyawt4945@refbux.com','ugqrdg7235@saabohio.com','enphov8475@woxgreat.com','ecvrzfh480@nowlike.com']
ARR2=['Hello','How are U','AAAA','1234','ssss','0921','1111111','......','8784892','aaaaazzzzzzzz','Hi']
# --------------------------------Login ti mediafire-----------------------------------#
driver.get('https://www.mediafire.com/login/')
driver.maximize_window()
MFemail=WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="widget_login_email"]')))
MFemail.send_keys('leheca1303@64ge.com')
MFpass=WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="widget_login_pass"]')))
MFpass.send_keys('*7N6H&b)94Dg4ga')
MFlogin=WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="form_login1"]/button')))
MFlogin.click()
#-----------------------------------chek mediafire--------------------------------------#
# MFcancel=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/button')
# MFcancel.click()
# time.sleep(5)
MFdismiss=WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div/div/div/div[3]/button[2]')))
MFdismiss.click()
MFbtn=WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[6]/div/div/div[4]/button[2]')))
MFbtn.click()
MFdsp=WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/button[7]')))
MFdsp.click()
MFdsp_input=WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div/div/div/div[2]/div[2]/input')))
MFinput = MFdsp_input.get_attribute('value')
MFnewinput2 = int(MFinput) + 1
pyperclip.copy(MFnewinput2)
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','v')
MFok=WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div/div/div/div[3]/button[1]')))
MFok.click()
#------------------------------------Login to Facebook-----------------------------------#
driver.get('https://web.facebook.com/login.php?skip_api_login=1&api_key=2081111558871624&kid_directed_site=0&app_id=2081111558871624&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D2081111558871624%26redirect_uri%3Dhttps%253A%252F%252Fauth.booyah.live%252Foauth%252Flogin%252Ffacebook%26response_type%3Dtoken%26scope%3Dpublic_profile%252Cemail%26state%3Dclient_id%25253D10058%252526redirect_uri%25253Dhttps%2525253A%2525252F%2525252Fbooyah.live%2525252Flogin%252526response_type%25253Dtoken%252526platform%25253D3%252526locale%25253Den-GB%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4c25334c-7d9a-4127-ab6b-8293ba4cad9d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.booyah.live%2Foauth%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dclient_id%25253D10058%252526redirect_uri%25253Dhttps%2525253A%2525252F%2525252Fbooyah.live%2525252Flogin%252526response_type%25253Dtoken%252526platform%25253D3%252526locale%25253Den-GB%23_%3D_&display=page&locale=en_GB&pl_dbl=0&_rdc=1&_rdr')
input1=WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="email"]')))
input1.send_keys(ARR1[int(MFinput)])
input2=WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="pass"]')))
input2.send_keys(')a&W,9Z;M2gUENf')
login=WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="loginbutton"]')))
login.click()
#-------------------------------------Go to Booyah---------------------------------------#
time.sleep(30)
driver.get('https://booyah.live/channels/9941224')
#BYlogin=WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/header/div/div/div[4]/button')))
#BYlogin.click()
#BYfb=WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div/div/div[2]/div/div[2]/div[3]/button')))
#BYfb.click()

chat=WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[4]/div[1]/div/div/div[4]/div[2]/div[1]/textarea')))
chatsend=WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[4]/div[1]/div/div/div[4]/div[2]/div[2]/button')))
time.sleep(2)
while True:
    chat.send_keys(ARR2[random.randint(0,10)])
    chatsend.click()
    time.sleep(random.randint(30,120))