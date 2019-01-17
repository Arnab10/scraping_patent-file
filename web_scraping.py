from selenium import webdriver
import time
import os
os.environ['MOZ_HEADLESS'] = '1'
plist = ["7,811,611","8012515","7976828","7867948","8,202,545","8202906","8329230","8,618,050","8,513,456","8802163"]
print("Welcome to US patent office : \n")
count = 1
for id in plist:
    print("\nPatent ",str(count),"\n\n")
    count = count+1
    driver = webdriver.Firefox(executable_path='/home/arnab/Downloads/geckodriver')
    time.sleep(2)   
    driver.get('http://patft.uspto.gov/netahtml/PTO/search-bool.html')
    time.sleep(5)

    driver.find_element_by_xpath("//*[@id='fld2']").send_keys("P")
    time.sleep(2)
    term = driver.find_element_by_xpath("//input[@id='trm2']")
    term.send_keys(id)

    button = driver.find_element_by_xpath("//input[@type='SUBMIT']")
    button.click()

    time.sleep(5)

    title=driver.find_element_by_xpath("//font[@size='+1']")
    print("Title : ",title.text)
    time.sleep(2)

    abstract = driver.find_element_by_xpath("//body[@bgcolor='#FFFFFF']/p")
    print("\nAbstract : ",abstract.text)
    time.sleep(2)

    inventors = driver.find_element_by_xpath("//td[@width = '90%' and @align='left']")
    print("\nInventors : ",inventors.text)
    time.sleep(2)

    fildate = driver.find_elements_by_xpath("//td[@width = '90%' and @align='left']")[3]
    print("\nFile Date : ",fildate.text)
    time.sleep(2)
    driver.close()
    print("\n\n ***********************")
    time.sleep(2)


 
