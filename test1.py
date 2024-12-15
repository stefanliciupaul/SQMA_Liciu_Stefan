from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service("C:\\Ruby33-x64\\bin\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:

    driver.get("http://collaborative.ase.ro/Pasul1.0.aspx")
    sleep(2)


    radio_button2 = driver.find_element(By.ID, "RadioButton2")
    radio_button2.click()
    sleep(2)
    next_button = driver.find_element(By.ID, "Button1")
    next_button.click()


    checkboxes = ["CheckBoxList1_0", "CheckBoxList1_4", "CheckBoxList1_9"]
    for checkbox_id in checkboxes:
        checkbox = driver.find_element(By.ID, checkbox_id)
        checkbox.click()
    sleep(2)

    listbox = Select(driver.find_element(By.ID, "ListBox1"))
    listbox_values = [
        "1.1. Aparate frigorifice de mari dimensiuni",
        "1.3. Aparate frigorifice / Congelatoare",
        "1.10. Plite electrice"
    ]

    for value in listbox_values:
        listbox.select_by_value(value)
    sleep(2)
    next_button = driver.find_element(By.ID, "Button1")
    next_button.click()
    sleep(2)
    checkbox = driver.find_element(By.ID, "CheckBoxList1_1")

    checkbox.click()

    sleep(2)

    listbox = Select(driver.find_element(By.ID, "ListBox1"))
    listbox_values = [
        "2.2. Volumul (cantitatea) de DEEE tratate",
        "2.7. Consumul de energie pe unitatea de DEEE reciclat",
    ]

    for value in listbox_values:
        listbox.select_by_value(value)
    sleep(2)
    next_button = driver.find_element(By.ID, "Button1")
    next_button.click()

    textbox_ids = ["TextBox00", "TextBox01", "TextBox10", "TextBox11", "TextBox20", "TextBox21"]
    for i, textbox_id in enumerate(textbox_ids, start=1):
        textbox = driver.find_element(By.ID, textbox_id)
        textbox.send_keys(str(i))
    sleep(2)
    next_button = driver.find_element(By.ID, "Button1")
    next_button.click()

    next_button = driver.find_element(By.ID, "Button1")
    next_button.click()
    sleep(2)
    textbox = driver.find_element(By.NAME, "ctl21")

    textbox.send_keys("9")

    complete_button = driver.find_element(By.NAME, "ctl25")
    complete_button.click()

    next_button = driver.find_element(By.ID, "Button1")
    next_button.click()
    sleep(2)


    export_button = driver.find_element(By.ID, "Button1")
    export_button.click()
    sleep(2)

finally:
    driver.quit()