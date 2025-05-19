from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Cấu hình trình duyệt
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

time.sleep(2)

# Nhập một phần thông tin (bỏ qua email và số điện thoại)
driver.find_element(By.ID, "firstName").send_keys("John")
driver.find_element(By.ID, "lastName").send_keys("Doe")

# Không chọn giới tính, không nhập số điện thoại
# Chỉ thử bấm Submit
submit_btn = driver.find_element(By.ID, "submit")
submit_btn.click()

time.sleep(2)

# Kiểm tra xem form không bị submit thành công
assert "Thanks for submitting the form" not in driver.page_source
print(" Form không được submit do thiếu thông tin")

driver.quit()
