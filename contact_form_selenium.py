#importing relevant packages to perform the activity
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

path = "/Users/arpitpaltani/Desktop/Selenium/chromedriver"
driver = webdriver.Chrome(path)

driver.get("http://www.webninjaz.com") #This command will open the browser and will load the website

driver.implicitly_wait(10) #wait for 10 seconds

contact_us = driver.find_element_by_id("menu-item-374") # Getting to the contact page
actions = ActionChains(driver)
actions.click(contact_us) #Defining the click function
actions.perform() # Performing the click action on the website

#filling up the contact form
driver.find_element_by_name("name1").send_keys("Arpit Paltani")
driver.find_element_by_name("email1").clear()
driver.find_element_by_name("email1").send_keys("arpit@webninjaz.com")
driver.find_element_by_name("mobile").send_keys("+91-9999822204")
driver.find_element_by_name("subject").send_keys("this is a bot developed by arpit")
driver.find_element_by_name("message").send_keys("this is a bot designed and developed by arpit paltani")

driver.find_element_by_xpath("//*[@id='contact-sec']/div/div[6]/div/input").click() # Getting the submit button to submit the form

driver.implicitly_wait(20)  # wait for 20 seconds
driver.quit() # This step will close the browser 
