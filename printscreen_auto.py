from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

### Images sequencer
count = int(1)

### URL list to get print
listaURL = ["https://console-openshift-console.apps.paas.domain.lab/dashboards",
            "https://console-openshift-console.apps.paas.domain.lab/settings/cluster/clusteroperators",
            "https://console-openshift-console.apps.paas.domain.lab/k8s/cluster/nodes"]


for URL in listaURL:

    ### Handle Insecure Certs
    options = webdriver.ChromeOptions()
    options.set_capability("acceptInsecureCerts",True)
    driver = webdriver.Chrome(options=options)

    ### Authentication
    driver.maximize_window()
    driver.get(URL)
    time.sleep(5)
    username_input = driver.find_element(By.ID,'inputUsername')
    password_input = driver.find_element(By.ID, 'inputPassword')
    username_input.send_keys('USUARIO')
    password_input.send_keys('SENHA')
    password_input.send_keys(Keys.ENTER)

    ### Printscreen process
    time.sleep(5) # Wait 5s to load the page
    driver.implicitly_wait(20) # Is not working
    driver.save_screenshot("screenshot-{}.png".format(count))
    count +=1

driver.quit()