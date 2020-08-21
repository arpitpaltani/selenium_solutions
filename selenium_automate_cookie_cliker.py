#importing relevant packages to perform the activity
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

Path = "/Users/arpitpaltani/Desktop/Selenium/chromedriver"
driver = webdriver.Chrome(Path)
driver.get("https://orteil.dashnet.org/cookieclicker/") #This command will open the browser and will load the website

driver.implicitly_wait(10) # Wait for 10 seconds to load the website

cookie = driver.find_element_by_id("bigCookie") # Finding cookie

cookie_count = driver.find_element_by_id("cookies") # Getting count of the coookies clicked

# Getting products to purchase
items = [driver.find_element_by_id("productPrice"+ str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(100):
    actions.perform() # Click the cookie
    count = int(cookie_count.text.split(" ")[0])
    #print("count",count)
    for item in items:
        value = int(item.text)
        #print("Value", value)
        if value <= count: #Finding products which has value less then cookie count
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform() #click the value 
driver.quit() # Close the browser
