import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.by import By

driver.get("http://suninjuly.github.io/cats.html")


# time.sleep(2)
# bullet_cat = driver.find_element(By.XPATH, "(//button[contains(text(),'View')])[1]").click()
# time.sleep(2)
# bullet_cat_text = driver.find_element(By.XPATH, '//p[text()="Bullet cat"]').text
# assert bullet_cat_text == "Bullet cat", "Wrong text!"

def test_text():
    time.sleep(1)
    bullet_cat_text = driver.find_element(By.XPATH, '//p[text()="Bullet cat"]').text
    assert bullet_cat_text == "Bullet cat", "Wrong text!"
    time.sleep(1)
    driver.quit()


