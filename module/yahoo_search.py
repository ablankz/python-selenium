from selenium import webdriver
from selenium.webdriver.common.by import By

# driver作成
driver = webdriver.Chrome()
# yahooの検索ページにアクセス
driver.get("https://www.yahoo.co.jp/")

# 検索ボックスのXPath
input_x_full_path = "/html/body/div[1]/div[1]/header/section[1]/div/form/fieldset/span/input"
# 検索ボタンのXPath
button_x_full_path = "/html/body/div[1]/div/header/section[1]/div/form/fieldset/span/button"

# 検索ボックスの取得
input_box = driver.find_element(by=By.XPATH, value=input_x_full_path)
# 検索文字列代入
input_box.send_keys("Python selemium 使い方")
# 検索ボタンの取得
search_button = driver.find_element(by=By.XPATH, value=button_x_full_path)
# 検索ボタンのクリック
search_button.click()

input("待機中")

driver.quit()